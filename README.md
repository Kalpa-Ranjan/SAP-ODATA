



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGZAZOZR%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T011445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rxzIItAL6Op2cFiaE7WsaLCsvmEx1GUtGUZ1sHwcgwIgLopMhrE1Y%2FojkYclay267zWQyMeZvWmNm5YEenbP5KEq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDCA4ZGeA0zSLsCtQLyrcA60ns%2F21v8j%2FRq0swknjKEkvEMmAXzI2qAiA4fMbWIgCJ%2Bb4664OPcTKmw6UQgW1eDbVhVmAD20zoX2mq0OOdP3dl4%2BCcyhLjAPkmIIk%2FcLQX9XGCi8jxNQIoTT%2BKEGxfmbYfqbnhYEKwt42GAK71EKM7%2FjsnmRBiZ0AzWkon7cMfv0b29FH4BudmsVTVYwvZLHEG%2BuJqELKioihQcdyoAS9MTR%2FMzUdBexE%2FwV2FPzL4hHhp%2BR%2FjsnAYQALW2av%2BWOLqSncN0hIfbLrLafbSDH1BhtsBrv%2Fxh0YKNWaQN8n5G64sdxTVM%2BxtWBi58YWPxhyF8Muv4Ar3jvTAKXR%2FOZV%2FNXKhjOe7fHrLuT5GVa91tIQkeiLEm9x6%2BpPimOoMk%2BxoSZ04tV%2BQozZ%2FIYF%2Bg%2FjlSZtwO48HP2ItihUqoBd%2BDImm1yBW5de%2BaIMvoDZoOvuTV2gDT3XiF3cXzsLHQdYaDBtF9SY8LWgCn48%2F9YKm0yFPQS1ZkUBRPbayYBYAl4jak%2BOhHBSPTAfvGh82805jdq1eEES%2BNHct4nr8vhYV4YEfyOFnh0%2FEKGaQ08jJPiy0JDq1j2pHpL4wdLV7Tnwb0Xqt0Piq4P1pi%2B9IhSdlTe0TpzIsLGDcl1WMPjKu8oGOqUBk9ecpY4VJsLvUf1Ya689eKu0vK6IvHjLyWXO%2FcpTZrnI0ZmiifTCKSNiO7R9%2Bej3S5IQskJCmfSidsuBpZI5PecM0OcwqmKMq8rEMS046bkv6GMfxxlZivSRtKfh6XKmj9BR%2FAgo5hi5BFt%2FnvCVvR9CWYxQLc2BT3zYPonyVdqrhHn2OpvKyLNaRm24bn%2B5hIN%2FbJSIyC8ps82MIUVX5rZikcpp&X-Amz-Signature=e7ef089a514d3b25539750354a2392310a824648e143d843eb328df630a28c3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGZAZOZR%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T011445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7rxzIItAL6Op2cFiaE7WsaLCsvmEx1GUtGUZ1sHwcgwIgLopMhrE1Y%2FojkYclay267zWQyMeZvWmNm5YEenbP5KEq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDCA4ZGeA0zSLsCtQLyrcA60ns%2F21v8j%2FRq0swknjKEkvEMmAXzI2qAiA4fMbWIgCJ%2Bb4664OPcTKmw6UQgW1eDbVhVmAD20zoX2mq0OOdP3dl4%2BCcyhLjAPkmIIk%2FcLQX9XGCi8jxNQIoTT%2BKEGxfmbYfqbnhYEKwt42GAK71EKM7%2FjsnmRBiZ0AzWkon7cMfv0b29FH4BudmsVTVYwvZLHEG%2BuJqELKioihQcdyoAS9MTR%2FMzUdBexE%2FwV2FPzL4hHhp%2BR%2FjsnAYQALW2av%2BWOLqSncN0hIfbLrLafbSDH1BhtsBrv%2Fxh0YKNWaQN8n5G64sdxTVM%2BxtWBi58YWPxhyF8Muv4Ar3jvTAKXR%2FOZV%2FNXKhjOe7fHrLuT5GVa91tIQkeiLEm9x6%2BpPimOoMk%2BxoSZ04tV%2BQozZ%2FIYF%2Bg%2FjlSZtwO48HP2ItihUqoBd%2BDImm1yBW5de%2BaIMvoDZoOvuTV2gDT3XiF3cXzsLHQdYaDBtF9SY8LWgCn48%2F9YKm0yFPQS1ZkUBRPbayYBYAl4jak%2BOhHBSPTAfvGh82805jdq1eEES%2BNHct4nr8vhYV4YEfyOFnh0%2FEKGaQ08jJPiy0JDq1j2pHpL4wdLV7Tnwb0Xqt0Piq4P1pi%2B9IhSdlTe0TpzIsLGDcl1WMPjKu8oGOqUBk9ecpY4VJsLvUf1Ya689eKu0vK6IvHjLyWXO%2FcpTZrnI0ZmiifTCKSNiO7R9%2Bej3S5IQskJCmfSidsuBpZI5PecM0OcwqmKMq8rEMS046bkv6GMfxxlZivSRtKfh6XKmj9BR%2FAgo5hi5BFt%2FnvCVvR9CWYxQLc2BT3zYPonyVdqrhHn2OpvKyLNaRm24bn%2B5hIN%2FbJSIyC8ps82MIUVX5rZikcpp&X-Amz-Signature=aea548c0e8aa4c14d70dfccb707e4e77d2c8742da252a2acf7e83f024ff2d888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







