*** Settings ***
Library           OperatingSystem

*** Test Cases ***
Example Test Case 1
    [Documentation]    This is a simple test case that checks if a file exists.
    [Tags]    example
    Create File    example.txt
    File Should Exist    example.txt
    Remove File    example.txt

Example Test Case 2
    [Documentation]    This test case creates a directory and verifies its existence.
    [Tags]    example
    Create Directory    example_dir
    Directory Should Exist    example_dir
    Remove Directory    example_dir

Example Test Case 3
    [Documentation]    This test case removes a directory and verifies its removal.
    [Tags]    example
    Create Directory    example_dir
    Remove Directory    example_dir
    Directory Should Not Exist    example_dir

Example Test Case 4
    [Documentation]    This test case renames a file and verifies the new name.
    [Tags]    example
    Create File    old_name.txt
    Move File    old_name.txt    new_name.txt
    File Should Exist    new_name.txt
    Remove File    new_name.txt

Example Test Case 5
    [Documentation]    This test case creates a file, writes to it, and verifies the content.
    [Tags]    example
    Create File    example.txt
    Append To File    example.txt    Hello, World!
    Should Contain    example.txt    Hello, World!
    Remove File    example.txt

Example Test Case 6
    [Documentation]    This test case verifies the existence of a non-existent file..
    [Tags]    example
    File Should Not Exist    non_existent_file.txt
