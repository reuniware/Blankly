"""
    Metrics wrapper for backtesting
    Copyright (C) 2021  Brandon Fan, Emerson Dove

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import blankly.metrics as metrics
from blankly.utils.time_builder import build_year


def cagr(backtest_data):
    account_values = backtest_data['resampled_account_value']
    years = (account_values['time'].iloc[-1] - account_values['time'].iloc[0]) / build_year()
    return round(metrics.cagr(account_values['value'].iloc[0], account_values['value'].iloc[-1], years), 2) * 100


def cum_returns(backtest_data):
    account_values = backtest_data['resampled_account_value']
    return round(metrics.cum_returns(account_values['value'][0], account_values['value'].iloc[-1]), 2) * 100


def sortino(backtest_data):
    # TODO: Need to pass in the specific resolution
    # Defaulting to 1d
    returns = backtest_data['returns']['value']
    return round(metrics.sortino(returns), 2)


def sharpe(backtest_data):
    # TODO: Need to pass in the specific resolution
    # Defaulting to 1d
    returns = backtest_data['returns']['value']
    return round(metrics.sharpe(returns), 2)


def calmar(backtest_data):
    # TODO: Need to pass in the specific resolution
    # Defaulting to 1d
    returns = backtest_data['returns']['value']
    return round(metrics.calmar(returns), 2)


def volatility(backtest_data):
    returns = backtest_data['returns']['value']
    return round(metrics.volatility(returns), 2)


def variance(backtest_data):
    returns = backtest_data['returns']['value'] * 100
    return round(metrics.variance(returns), 2)


def beta(backtest_data):
    # TODO: Need to pass in the specific resolution
    # Defaulting to 1d
    # Need to get some sort of baseline for this one...
    # Use SP500 as default for all of them (can we get this data?)
    # Or pick one of the assets as a baseline
    returns = backtest_data['returns']['value']
    return round(metrics.beta(returns), 2)


def var(backtest_data):
    returns = backtest_data['returns']['value']
    account_values = backtest_data['resampled_account_value']
    return round(metrics.var(account_values['value'][0], returns, 0.95), 2)


def cvar(backtest_data):
    returns = backtest_data['returns']['value']
    account_values = backtest_data['resampled_account_value']
    return round(metrics.cvar(account_values['value'][0], returns, 0.95), 2)


def max_drawdown(backtest_data):
    values = backtest_data['returns']['value']
    return abs(round(metrics.max_drawdown(values), 2)) * 100
