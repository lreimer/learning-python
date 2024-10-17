#!/usr/bin/env molotov -v -r 100
# -*- coding: utf-8 -*-
import molotov

"""
Monolov load test for the QAware website.
Weight is set to 25 for the scenario.
"""
@molotov.scenario(25)
async def scenario_qaware(session):
    async with session.get("https://www.qaware.de") as resp:
        assert resp.status == 200

"""
Monolov load test for the Microservice demo.
Weight is set to 75 for the scenario.
"""
@molotov.scenario(75)
async def scenario_demo(session):
    async with session.get("https://learning-python-1091663571214.europe-north1.run.app") as resp:
        assert resp.status == 200
        
        body = await resp.json()
        assert body["message"] == "Hello World!"
