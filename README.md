



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U42RG4X3%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T180530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FTvH2H5MN8jUmDIxfMNs4VPalnzCvCDlf3tzSGdzGxAiBd6nk3IoM0UWzQGB8VXwkdrUo9WZiBYSBo6eymqg5xeyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMgr4%2BmoQIUxHivcXeKtwDdJPMttQc6AvtnIh506oYt3mQ2rh3XgB%2FzffMusGpNV0W2XOwjrpDTYh6V12q%2FbzigxCasJ6srBhPONSA74BxJQj6%2B8ahVLA3%2FFNaTedwP1Ub6rybllUcOfRsceS2XXkHcp%2BX5QNFhWP0anOq8M1BCJ5k%2FzoWSOIxf7sqBew05WhXt1mpEcnIY8fY7p5ktBfNK6qId%2B4HlBdf7uPuaJX5O2QX8JoStk8cP%2Bi2GqynnA7CvkdY5ug4L4FbG0gOQA%2FRPqE1MU%2FZEkmQcVn%2FeqqxaDtVR1y6Sbu7t3DHltyqaQdykxf0S6d3XGvpj92nLSvWusUbadj5mDk%2F%2B13dMoSiGs7dAAmsOGdaZccVzveNkOUbmGUrsqWDBbXJfmw90UIX8%2BoUX%2BDxbg7vLgTyYBZhgluko2HQ1H%2F8d6aYHeiYebrEJsGdc%2Bl0CeTCrdK9iQFUJ%2BctuyMUxmWu6PwoyFDtkEYpl3OgDiSaVfbyhiP2SKLzKLjr4TQ0OzQN7IVMDJq%2FGt%2BQsJ0D3N2rgkA0udmkGUXIikInaB5g92bqC7vQBEFvlGUvLsCMtZap0%2BZtC6yuI0t40iqj35m492G1e0TD%2Be7zQTu3EavaM3qCxXfQ3OgjpZIrfCpT6jroywAwzL3S1wY6pgHlDOVyCL%2F1ReXx6eV4eODytmkCkAuD5J%2FUpvOFQ%2FmJRfBchubU50XgFDJCEzHX%2F3nti6EnU574yPV5YAaCPrpAYXU0qDaCu32kdyOX1Y2Sik28FcsRsN5MbXco5h12h5iimPl2%2BQ10Ex1m6dmHytztud08%2FV95r8wlG286guDrew534r%2BUpcVSzGKiRn1Rd8zz8Ua2ScT%2FeHteAQr2KSInEtd2%2Bcz0&X-Amz-Signature=4c35eb8ed122129e9d3d4e492842b72d655e8b0370777369a1ee4575d720e14a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U42RG4X3%2F20261111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261111T180530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FTvH2H5MN8jUmDIxfMNs4VPalnzCvCDlf3tzSGdzGxAiBd6nk3IoM0UWzQGB8VXwkdrUo9WZiBYSBo6eymqg5xeyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMgr4%2BmoQIUxHivcXeKtwDdJPMttQc6AvtnIh506oYt3mQ2rh3XgB%2FzffMusGpNV0W2XOwjrpDTYh6V12q%2FbzigxCasJ6srBhPONSA74BxJQj6%2B8ahVLA3%2FFNaTedwP1Ub6rybllUcOfRsceS2XXkHcp%2BX5QNFhWP0anOq8M1BCJ5k%2FzoWSOIxf7sqBew05WhXt1mpEcnIY8fY7p5ktBfNK6qId%2B4HlBdf7uPuaJX5O2QX8JoStk8cP%2Bi2GqynnA7CvkdY5ug4L4FbG0gOQA%2FRPqE1MU%2FZEkmQcVn%2FeqqxaDtVR1y6Sbu7t3DHltyqaQdykxf0S6d3XGvpj92nLSvWusUbadj5mDk%2F%2B13dMoSiGs7dAAmsOGdaZccVzveNkOUbmGUrsqWDBbXJfmw90UIX8%2BoUX%2BDxbg7vLgTyYBZhgluko2HQ1H%2F8d6aYHeiYebrEJsGdc%2Bl0CeTCrdK9iQFUJ%2BctuyMUxmWu6PwoyFDtkEYpl3OgDiSaVfbyhiP2SKLzKLjr4TQ0OzQN7IVMDJq%2FGt%2BQsJ0D3N2rgkA0udmkGUXIikInaB5g92bqC7vQBEFvlGUvLsCMtZap0%2BZtC6yuI0t40iqj35m492G1e0TD%2Be7zQTu3EavaM3qCxXfQ3OgjpZIrfCpT6jroywAwzL3S1wY6pgHlDOVyCL%2F1ReXx6eV4eODytmkCkAuD5J%2FUpvOFQ%2FmJRfBchubU50XgFDJCEzHX%2F3nti6EnU574yPV5YAaCPrpAYXU0qDaCu32kdyOX1Y2Sik28FcsRsN5MbXco5h12h5iimPl2%2BQ10Ex1m6dmHytztud08%2FV95r8wlG286guDrew534r%2BUpcVSzGKiRn1Rd8zz8Ua2ScT%2FeHteAQr2KSInEtd2%2Bcz0&X-Amz-Signature=9c933e6072f3574b67b1e7912213bcff8682d86dafbac3bb63b1f4ea3cf3b1b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







