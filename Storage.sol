// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ZARCStorage {
    string public myMessage;

    function setMessage(string memory _text) public {
        myMessage = _text;
    }
}
