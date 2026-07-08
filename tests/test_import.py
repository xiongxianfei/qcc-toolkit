def test_package_imports() -> None:
    import qcc_toolkit

    assert isinstance(qcc_toolkit.__version__, str)
    assert qcc_toolkit.__version__
