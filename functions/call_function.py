def call_function(function_call_part, verbose=False):
    fn_name = function_call_part.name
    fn_args = function_call_part_args.copy()
    if verbose:
        print(f"Calling function: {fn_name}({fn_args})")
    else:
        print(f" - Calling function: {fn_name}")
    
    fn_args["working_directory"] = "./calculator"

    functions = {
        "call_function": call_function,
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if fn_name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=fn_name,
                    response={"error": f"Unknown function: {fn_name}"},
                )
            ],
        )

    function_result = functions[fn_name]

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=fn_name,
            response={"result": function_result},
        )
    ],
)
