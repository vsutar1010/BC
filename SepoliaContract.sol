// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract SepoliaContract {

    string public message = "Hello Sepolia";

    function setMessage(string memory newMessage) public {
        message = newMessage;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}