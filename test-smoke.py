from app import add, main

def test_add():
    assert add(2, 3) == 5

def test_main_runs():
    # Just make sure it executes without throwing
    main()