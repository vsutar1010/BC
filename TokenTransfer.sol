// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract TokenTransfer {

    mapping(address => uint) public balances;

    constructor() {
        balances[msg.sender] = 100;
    }

    function transfer(address receiver, uint amount) public {

        require(
            balances[msg.sender] >= amount,
            "Insufficient balance"
        );

        balances[msg.sender] -= amount;

        balances[receiver] += amount;
    }
}