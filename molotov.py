#!/usr/bin/env molotov -v -r 100
# -*- coding: utf-8 -*-
import molotov

"""
Monolov load test for the QAware website.
Weight is set to 100 for the scenario.
"""
@molotov.scenario(100)
async def scenario_qaware(session):
    async with session.get("https://www.qaware.de") as resp:
        assert resp.status == 200

