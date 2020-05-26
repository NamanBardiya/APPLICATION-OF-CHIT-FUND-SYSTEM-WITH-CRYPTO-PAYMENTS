import React, {useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import win from '../assets/win.png';
import betterluck from '../assets/betterluck.png';
import { API_BASE_URL, BID } from '../config';


function ChitFund() {
    const [luckyAddress, setLuckyAddress] = useState('');
    const [ knownAddresses, setKnownAddresses] = useState([]);
    const [walletInfo, setWalletInfo] = useState({});
    
    useEffect(() => {
        fetch(`${API_BASE_URL}/chit-fund`)
        .then((response) => response.json())
        .then(json => setLuckyAddress(json));
    }, []);
    
    useEffect(() => {
        fetch(`${API_BASE_URL}/known-addresses`)
        .then(response => response.json())
        .then(json => setKnownAddresses(json));
    }, []);
    
    useEffect(() => {
        fetch(`${API_BASE_URL}/wallet/info`)
        .then((response) => response.json())
        .then(json => setWalletInfo(json));
    }, []);
    
    const {address,balance} = walletInfo;
    
    return(
    <div className="App">
        <Link to="/">Home</Link>
        <div>
        Bid Amount: {BID} 
        <br />Collected Amount: {knownAddresses.length*BID}
        <b><br />Winning Amount: {0.9*knownAddresses.length*BID}</b>
        <br />
        {address === luckyAddress ? <img className="logo" src={win} alt="Congratulations! You won" /> : <img className="logo" src={betterluck} alt="Sorry! Better luck next time" />}
        <br />
        <h3>
        {address === luckyAddress ? 'Congratulations! You won':'Better Luck Next Time!'}
        </h3>
        <br />
        <h3>Congratulations {luckyAddress} !!!</h3>
        <hr />
        {luckyAddress} will be receiving the winning amount soon. 
        <br />The winning amount is 90% of total collected amount. 
        <br />Rest 10% would be distributed among other suscribers of Chit Fund.
        </div>
        
      </div>
  );
}

export default ChitFund;
