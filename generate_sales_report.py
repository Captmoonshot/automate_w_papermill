from sys import argv
import papermill as pm

def main():
    script, input_file, output_file, filename = argv
    resp = None
    resp = make_report(
        input_file,
        output_file,
        filename
    )
    if resp is not None:
        print("\nSuccess!\n")
    else:
        print("Failed to generate Sales Report.")

def make_report(input_f, output_f, f):
    resp = pm.execute_notebook(
        input_f,
        output_f,
        parameters=dict(filename=f)
    )
    return resp

if __name__ == "__main__":
    main()



