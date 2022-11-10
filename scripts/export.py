import os
import glob
import subprocess
import shutil
import optparse
import pprint

# folders from the blocklist are deleted
blocklist = [
    "notebooks/exercises/churn",
    "notebooks/exercises/pelf",
    "notebooks/.assets/data/churn",
    "notebooks/.assets/data/pelf",
]

def remove_blocklisted(export_dir):
    """Remove folders on blocklist from export"""
    for dir_path in blocklist:
        try:
            print(f"BLACKLIST REMOVE: {dir_path}")
            shutil.rmtree(os.path.join(export_dir, dir_path))
        except:
            print(f"BLACKLIST REMOVE FAILED: {dir_path}")

def remove_pycache(export_dir):
    """Remove folders __pycahce__ in all folders"""
    for root, dir_path, subdirs in os.walk(export_dir):
        for d in dir_path:
            #print(root, dir_path, subdirs, d)
            if d == "__pycache__":
                shutil.rmtree(os.path.join(root, d))
                print(f"DEL PYCACHE FOLDER IN: {root}")
    print('DEL PYCACHE FOLDERS FINSISHED')

def copy_notebooks(proj_dir, export_dir):
    """Copy the notebooks"""
    nb_dir = os.path.join(proj_dir, "notebooks")
    nb_export_dir = os.path.join(export_dir, "notebooks")
    shutil.copytree(nb_dir, nb_export_dir)

def export_html(export_dir):

    list_of_nbs = list(
            glob.iglob(
                f"{export_dir}/notebooks/**/*.ipynb",
                recursive=True
            )
        )
    wip_nbs = list(
        glob.iglob(
            f"{export_dir}/notebooks/**/wip_*.ipynb"
        )
    )
    list_of_nbs = sorted(list(set(list_of_nbs) - set(wip_nbs)))
    error_nbs = []
    print("converting notebooks:")
    pprint.pprint(list_of_nbs)

    # run notebooks before export
    for nb_path in list_of_nbs:
        try:
            print(f"EXPORTING {nb_path}")
            # run notebook and export to html
            subprocess.call(
                f"jupyter nbconvert --ExecutePreprocessor.timeout=300 --execute --to html {nb_path}",
                shell=True
            )
            # Replace .ipynb file extension by .html for all link targets in html output file
            html_path = nb_path.replace(".ipynb", ".html")
            # Read in the file
            with open(html_path, 'r') as fn:
              filedata = fn.read()
            # Replace the target string
            filedata = filedata.replace(".ipynb", ".html")
            # Write the file out again
            with open(html_path, 'w') as fn:
              fn.write(filedata)
        except KeyboardInterrupt:
            print("ABORTED")
            return
        except:
            print(f"ERROR: {nb_path}")
            error_nbs.append(nb_path)
    print("DONE: notebooks exported")
    if error_nbs:
        print(f"ERROR: not exported: {error_nbs}")

def copy_library(proj_dir, export_dir):
    """Copy the library"""
    lib_dir = os.path.join(proj_dir, "library")
    export_dir = os.path.join(export_dir, "library")
    shutil.copytree(lib_dir, export_dir)
    shutil.copyfile("requirements.txt", f"{options.export_dir}/requirements.txt")
    shutil.copyfile("README.md", f"{options.export_dir}/REDME.md")
    shutil.copyfile("LICENSE", f"{options.export_dir}/LICENSE")

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option(
        "--export_dir",
        dest="export_dir",
        help="path to directory with the exported files"
    )
    parser.add_option(
        "--to_html",
        dest="to_html",
        action="store_true",
        default=False,
        help="flag for HTML export"
    )
    (options, args) = parser.parse_args()
    copy_notebooks('.', options.export_dir)
    copy_library('.', options.export_dir)
    remove_blocklisted(options.export_dir)
    if options.to_html:
        export_html(options.export_dir)
    remove_pycache(options.export_dir)
