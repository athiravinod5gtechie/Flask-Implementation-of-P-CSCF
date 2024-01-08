# Flask-Implementation : P-CSCF
A Sample Flask program with POST method and endpoint will be like npcf-policyauthorization/v1/app-sessions
(Reference : https://www.etsi.org/deliver/etsi_ts/129500_129599/129513/16.06.00_60/ts_129513v160600p.pdf) and response.

**Step 1**: Add app.py to your VM <br>
**Step 2**: Run it  (terminal 1 )<br>
        python3 app.py <br>
**Step 3**:  Test the response using curl <br>
        curl -X POST -H "Content-Type: application/json" -d '{"afAppId": "myApp", "afChargId": "myChargingId", "afReqData": "UE_IDENTITY"}' http://localhost:5000/npcf-policyauthorization/v1/app-sessions <br>

**Sample output snips and code file are added in this repo**

