import glob
import subprocess
import sys
import pprint

def test_notebooks():
    list_of_nbs = list(
            glob.iglob(
                f"notebooks/**/*.ipynb",
                recursive=True
            )
        )
    wip_nbs = list(
        glob.iglob(
            f"notebooks/**/wip_*.ipynb"
        )
    )


    list_of_nbs = sorted(list(set(list_of_nbs) - set(wip_nbs)))
    print("TESTING: ")
    pprint.pprint(list_of_nbs)
    if not len(list_of_nbs) > 0:
        print("ERROR: no notebooks found")
        sys.exit(1)

    error_nbs = []  # notebooks with errors

    # run notebooks before export
    for nb_path in list_of_nbs:
        try:
            print(f"EXPORTING {nb_path}")
            # run notebook and export to html
            exit_code =subprocess.call(
                f"jupyter nbconvert --ExecutePreprocessor.timeout=1200 --execute --clear-output {nb_path}",
                shell=True
            )
            if exit_code != 0:
                print(f"ERROR: {nb_path}")
                error_nbs.append(nb_path)
        except KeyboardInterrupt:
            print("ABORTED")
            return error_nbs
        except:
            print(f"ERROR: {nb_path}")
            error_nbs.append(nb_path)
    return error_nbs

if __name__ == "__main__":
    error_nbs = test_notebooks()
    if len(error_nbs) == 0:
        print("SUCCESS: all notebooks working")
        sys.exit(0)
    else:
        print("FAILURE: the following notebooks threw exceptions:")
        pprint.pprint(error_nbs)
        sys.exit(1)
