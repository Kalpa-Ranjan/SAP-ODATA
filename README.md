



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHQEB4K%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T182135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDx8eh5%2BIYNcGONM3nMMKVJKgRAL%2BrGadOwLL5ZoEC5AwIgN3H5NhfbC%2FVUV3bCk5yQyB9lxhMNer0cVE2V8WSiYV4q%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDIhX11%2FPP%2B0vko1I9SrcA5BVe%2BTzb4TOY64ArVfVQtyLj22377lq%2FV33LMdJ0sZvUDEatuci5u2cVPfOyw8wFx0Kla79ek%2Fbu1ItGdqHJqvtGP6seklNKfP84t2VkjB2rpsNI%2FFFkBD845poXFBPozvgmFm9wvDbic0%2FqhZYDW76EZo7ppG24tX6inFLOOmjNba5KXlis%2BNtFA1KdOb3TDcwsz8cgJc7fLrsCJ%2BgkEP6GNnkSTouqvvtJ%2BelYMqiqWfXO%2FPn4thYpCIgwxhyNUDenSsPi7IoXUIQoQ3ytIYLAMJdc%2FPD9RHBa2gWUe8gHfVA2c4y%2FhaRhTUS3JjXJwMDgiO5lv1ywJOTUFkTqfX8CkCpudIso2UBnEobpvDFDa0GTMQbNnQBB%2BG0%2BEElEcXraUlPz1tWjw7vgKEUwGAsF5uOTwwgblUUbvzsgEAXORJrCdTYGl59RDzG37RHroP8CPiRh2x2p38SNR77T%2BgpOzO6Xab2iDC1oH8ladu9jdxwTfPjpbwXJHPk7ACK094AqX4o3Nzvu7I6yE8%2F%2BGz5jBRBiV11636C6hdSxaRCmurqUvXsW019wkEuBYjYeCawwkHhwLYq59bH1To6o0cBcTXrjphGLpHHA82ElcKFBTyz907J0abyQjRxMOW%2BgskGOqUBczD1dhbmPmgtHEnA9egMtRftRqB90SSFBG85BM%2Fr1I4XnbWT51g%2F1H9TiqVnWMx0D2FMRITGEmySTybG6WsGPFpLZiNilGLXqjG1KTlm6k7mpirin1cLZ%2B9tPzJaYrgQH1XqqXgq3SV9IzCf6grN2V9na8uSO8v1XOWDkaEcCl1AOmpNzBa3wtoTSCOY8cewwmdhj5VYH3%2FXt4XmOo2Zsrd46fUS&X-Amz-Signature=a1847883973de0262be8790acaa14c4cd5e9a2844d5c9b4e0d17ad66c120e1cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZHQEB4K%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T182136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDx8eh5%2BIYNcGONM3nMMKVJKgRAL%2BrGadOwLL5ZoEC5AwIgN3H5NhfbC%2FVUV3bCk5yQyB9lxhMNer0cVE2V8WSiYV4q%2FwMIEhAAGgw2Mzc0MjMxODM4MDUiDIhX11%2FPP%2B0vko1I9SrcA5BVe%2BTzb4TOY64ArVfVQtyLj22377lq%2FV33LMdJ0sZvUDEatuci5u2cVPfOyw8wFx0Kla79ek%2Fbu1ItGdqHJqvtGP6seklNKfP84t2VkjB2rpsNI%2FFFkBD845poXFBPozvgmFm9wvDbic0%2FqhZYDW76EZo7ppG24tX6inFLOOmjNba5KXlis%2BNtFA1KdOb3TDcwsz8cgJc7fLrsCJ%2BgkEP6GNnkSTouqvvtJ%2BelYMqiqWfXO%2FPn4thYpCIgwxhyNUDenSsPi7IoXUIQoQ3ytIYLAMJdc%2FPD9RHBa2gWUe8gHfVA2c4y%2FhaRhTUS3JjXJwMDgiO5lv1ywJOTUFkTqfX8CkCpudIso2UBnEobpvDFDa0GTMQbNnQBB%2BG0%2BEElEcXraUlPz1tWjw7vgKEUwGAsF5uOTwwgblUUbvzsgEAXORJrCdTYGl59RDzG37RHroP8CPiRh2x2p38SNR77T%2BgpOzO6Xab2iDC1oH8ladu9jdxwTfPjpbwXJHPk7ACK094AqX4o3Nzvu7I6yE8%2F%2BGz5jBRBiV11636C6hdSxaRCmurqUvXsW019wkEuBYjYeCawwkHhwLYq59bH1To6o0cBcTXrjphGLpHHA82ElcKFBTyz907J0abyQjRxMOW%2BgskGOqUBczD1dhbmPmgtHEnA9egMtRftRqB90SSFBG85BM%2Fr1I4XnbWT51g%2F1H9TiqVnWMx0D2FMRITGEmySTybG6WsGPFpLZiNilGLXqjG1KTlm6k7mpirin1cLZ%2B9tPzJaYrgQH1XqqXgq3SV9IzCf6grN2V9na8uSO8v1XOWDkaEcCl1AOmpNzBa3wtoTSCOY8cewwmdhj5VYH3%2FXt4XmOo2Zsrd46fUS&X-Amz-Signature=a0ebed7f8c14c910ab44e5270fb6002eacac7d278b51594225689686b631bb80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







