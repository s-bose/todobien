import questionary
import argparse
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import CompleteStyle
import argcomplete

projects = {
    "show": {
        "version": None,
        "interfaces": None,
        "clock": None,
        "ip": {"interface": "Brief"},
    },
    "exit": None,
}

argparser = argparse.ArgumentParser()
completer = NestedCompleter.from_nested_dict(
    {
        "show": {"version": None, "clock": None, "ip": {"interface": {"brief"}}},
        "exit": None,
    }
)
argparser.add_argument("-p", "--path", required=False, choices=["a", "b", "c"])
argcomplete.autocomplete(argparser)

if __name__ == "__main__":
    args = argparser.parse_args()
    resp = None
    # if not args.path:
    #     resp = questionary.autocomplete(
    #         "select project: ",
    #         choices=projects.keys(),
    #         completer=completer,
    #         complete_style=CompleteStyle.MULTI_COLUMN,
    #     ).ask()
    # resp = questionary.autocomplete(
    #     "select task: ",
    #     choices=projects.get(resp or args.path),
    #     completer=completer,
    #     complete_style=CompleteStyle.MULTI_COLUMN,
    # ).ask()

    print(resp)
