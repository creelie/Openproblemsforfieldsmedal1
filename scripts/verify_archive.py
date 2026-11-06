"""Verify the public Zenodo archive corresponding to this exact GitHub release."""
import json
from pathlib import Path
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "creelie/Openproblemsforfieldsmedal1"
TAG = "v2.0.0"
TITLE = "Signed Liouville energies and the limits of maximal correlation bounds"


def records(query):
    endpoint = "https://zenodo.org/api/records?" + urlencode(
        {"q": query, "size": 10, "sort": "mostrecent"}
    )
    request = Request(endpoint, headers={"User-Agent": "RH-research-archive-verifier"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)["hits"]["hits"]


def matches(record):
    metadata = record.get("metadata", {})
    links = metadata.get("related_identifiers", [])
    repository_match = any(
        REPOSITORY.lower() in item.get("identifier", "").lower()
        and TAG in item.get("identifier", "")
        for item in links
    )
    return (repository_match and metadata.get("version") in ("2.0.0", TAG)
            and metadata.get("title", "").casefold() == TITLE.casefold())


def main():
    queries = [
        'related_identifiers.identifier:"https://github.com/' + REPOSITORY + '/tree/' + TAG + '"',
        '"' + TITLE + '"',
    ]
    for attempt in range(24):
        try:
            for query in queries:
                for record in records(query):
                    if not matches(record):
                        continue
                    doi = record.get("doi", "")
                    if not doi.startswith("10.5281/zenodo."):
                        raise ValueError("Unexpected DOI")
                    result = {
                        "repository": REPOSITORY, "tag": TAG,
                        "record_id": record["id"], "doi": doi,
                        "url": "https://doi.org/" + doi,
                        "zenodo_url": record["links"]["html"],
                        "version": record["metadata"]["version"],
                        "title": record["metadata"]["title"],
                        "files": [
                            {"key": f["key"], "checksum": f.get("checksum")}
                            for f in record.get("files", [])
                        ],
                    }
                    destination = ROOT / "docs" / "ZENODO-ARCHIVE.json"
                    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
                    print(json.dumps(result, indent=2))
                    return
        except Exception as error:
            print(type(error).__name__, str(error))
        if attempt < 23:
            time.sleep(15)
    raise SystemExit("The exact Zenodo archive has not yet been verified")


if __name__ == "__main__":
    main()
