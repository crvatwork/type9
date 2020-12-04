import pytest
import sys
import type9


def test_randomize_salt():
    salt = type9.randomize_salt()
    
    assert len(salt) == 14


def test_generate_hash():
    # $9$TP3XUYzdNFqb/i$Ecp24Hsm0DnbCIqsId9VmYJP4yFh/YmGZ5vMV93v.bA
    # $9$Fbk5Okjb1/tYvg$DI984NlnnJk404Fn6mdrLOk0UBEY5shdj6lPJIiHMQ.

    assert type9.generate_hash("TP3XUYzdNFqb/i", "cisco") == \
        "Ecp24Hsm0DnbCIqsId9VmYJP4yFh/YmGZ5vMV93v.bA"
    assert type9.generate_hash("Fbk5Okjb1/tYvg", "cisco") == \
        "DI984NlnnJk404Fn6mdrLOk0UBEY5shdj6lPJIiHMQ."


def test_generate_hash_mocked_0args(capsys, mocker):
    mocker.patch.object(
        sys,
        "argv",
        [
            "type9"
            ]
        )

    with pytest.raises(SystemExit) as pytest_wrapped_error:
        type9.main()

    assert pytest_wrapped_error.type is SystemExit
    assert pytest_wrapped_error.value.args[0] == \
        "This program accepts either a salt and a plain-text password or a plain-text password."


def test_generate_hash_mocked_1args(capsys, mocker):
    # $9$TP3XUYzdNFqb/i$Ecp24Hsm0DnbCIqsId9VmYJP4yFh/YmGZ5vMV93v.bA

    mocker.patch.object(
        sys,
        "argv",
        [
            "type9",
            "cisco"
            ]
        )

    type9.main()
    captured = capsys.readouterr()

    assert len(captured.out) == 62


def test_generate_hash_mocked_2args(capsys, mocker):
    # $9$Fbk5Okjb1/tYvg$DI984NlnnJk404Fn6mdrLOk0UBEY5shdj6lPJIiHMQ.

    mocker.patch.object(
        sys, 
        "argv",
        [
            "type9",
            "Fbk5Okjb1/tYvg",
            "cisco"
            ]
        )

    type9.main()
    captured = capsys.readouterr()

    assert captured.out == \
        "$9$Fbk5Okjb1/tYvg$DI984NlnnJk404Fn6mdrLOk0UBEY5shdj6lPJIiHMQ.\n"
