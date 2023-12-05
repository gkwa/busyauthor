def print_command_hierarchy(args):
    db_file = args.db
    command = getattr(args, "command", None)
    command_args = getattr(args, "command_args", None)
    subcommand = getattr(args, "subcommand", None)
    subcommand_args = getattr(args, "subcommand_args", None)
    subsubcommand = getattr(args, "subsubcommand", None)
    subsubcommand_args = getattr(args, "subsubcommand_args", None)
    subsubsubcommand = getattr(args, "subsubsubcommand", None)
    subsubsubcommand_args = getattr(args, "subsubsubcommand_args", None)

    print(f"Database File: {db_file}")

    if command:
        print(f"Command: {command}")
        print(f"Command Args: {command_args}")

        if subcommand:
            print(f"Subcommand: {subcommand}")
            print(f"Subcommand Args: {subcommand_args}")

            if subsubcommand:
                print(f"Subsubcommand: {subsubcommand}")
                print(f"Subsubcommand Args: {subsubcommand_args}")

                if subsubsubcommand:
                    print(f"Subsubsubcommand: {subsubsubcommand}")
                    print(f"Subsubsubcommand Args: {subsubsubcommand_args}")
