def print_command_hierarchy(args):
    db_file = args.db

    command = getattr(args, "command", None)
    command_args = getattr(args, "command_args", None)

    command2 = getattr(args, "command2", None)
    command2_args = getattr(args, "command2_args", None)

    subcommand = getattr(args, "subcommand", None)
    subcommand_args = getattr(args, "subcommand_args", None)

    subsubcommand = getattr(args, "subsubcommand", None)
    subsubcommand_args = getattr(args, "subsubcommand_args", None)

    subsubsubcommand = getattr(args, "subsubsubcommand", None)
    subsubsubcommand_args = getattr(args, "subsubsubcommand_args", None)

    subsubsubsubcommand = getattr(args, "subsubsubsubcommand", None)
    subsubsubsubcommand_args = getattr(args, "subsubsubsubcommand_args", None)

    print(f"Database File: {db_file}")

    if command:
        print(f"Command: {command}")
        print(f"Command Args: {command_args}")

        print(f"Command2: {command2}")
        print(f"Command2 Args: {command2_args}")

        if subcommand:
            print(f"Subcommand: {subcommand}")
            print(f"Subcommand Args: {subcommand_args}")

            if subsubcommand:
                print(f"Subsubcommand: {subsubcommand}")
                print(f"Subsubcommand Args: {subsubcommand_args}")

                if subsubsubcommand:
                    print(f"Subsubsubcommand: {subsubsubcommand}")
                    print(f"Subsubsubcommand Args: {subsubsubcommand_args}")

                    if subsubsubsubcommand:
                        print(f"Subsubsubsubcommand: {subsubsubsubcommand}")
                        print(f"Subsubsubsubcommand Args: {subsubsubsubcommand_args}")
