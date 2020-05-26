import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Switch, Route} from 'react-router-dom';
import history from './history';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransaction from './components/ConductTransaction';
import TransactionPool from './components/TransactionPool';
import ChitFund from './components/ChitFund';

ReactDOM.render(
  <Router history={history}>
    <Switch>
        <Route path='/' exact component={App} />
        <Route path='/blockchain' component={Blockchain} />
        <Route path='/conduct-transaction' component={ConductTransaction} />
        <Route path='/transaction-pool' component={TransactionPool} />
        <Route path='/chit-fund' component={ChitFund} />
    </Switch>
  </Router>,
  document.getElementById('root')
);

