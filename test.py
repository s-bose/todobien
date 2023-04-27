import questionary
import argparse

projects = {
    "todobien": [
        "TDB-001",
        "TDB-002",
        "TDB-003",
        "TDB-004",
    ],
    "fermit": [
        "FMT-001",
        "FMT-002",
        "FMT-003",
    ],
    "random": [
        "RND-42",
        "RND-44",
    ],
}

argparser = argparse.ArgumentParser()

argparser.add_argument("-p", "--path", required=False)

if __name__ == "__main__":
    args = argparser.parse_args()
    resp = None
    if not args.path:
        resp = questionary.autocomplete(
            "select project: ", choices=projects.keys()
        ).ask()
    resp = questionary.autocomplete(
        "select task: ", choices=projects.get(resp or args.path)
    ).ask()

    print(resp)
