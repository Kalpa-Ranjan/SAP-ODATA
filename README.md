



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624GMC3AV%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T061512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfkl009NaEEjQnmg0NJ9q%2Bup7ok4DIPz3d8%2F1S0fUKWAiBqfZsiairCzXzYuBkiBtEgeY35mg3H1Tae3OiJwJUI3iqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvUz6cXHQOfDj3TPvKtwDg%2Bsus9nu9uq5BKFjEqs7Bi8fL39pj3ELJv5oLnhncKjg1TSOfHxRRxHrZiBZrxLqF0KNN7fy7dEQdHBgk0bOBbg7QkASPSkykpZgeOZ%2Bs5vOcF5Q%2B64vShsLkRDZaNkXXMdYkdssA8cpRcVSN8yHTyvfxWgu4aDToxi0DEMNEryzbRioUJvn%2BeqVDFfYwsQyFCp3IXy0KkKyK%2FEGxuAhaaNF8XPDVEbYsuWeU9SwKY6wgdEclWPBZUNSz0%2Bt0SE1DM1dzZugGTXORcXbb2cEnKel99g1pr7xilqiBgULhJTtmiSOp5v550kPd6YkzrowBmNzD67KxR5a937Ti%2B83G0eWj6YNdBnULD4sgnJPV4EYdEQlUgdecykA%2FDRPpsbprl93e82Ct1m1vzWdjXUNQFX8E%2F8zloMsimI%2B5V4JsmFB5vqiycAm%2BZsuv94FYhYykPMSw83giiVeEfDBjibxhtozD0pbO3i4tzYbn2YZ677IL%2BUDaMZdkQ755QZEU%2FWfXrCF79zJlyuMZkHk3USxYiiTcGkYw56U%2FMwj9ds1dcBkRyZhb4PKE%2FBLjCUtZtdZ77NOLVTdd6YLwxrnxExgvYKDPll0q8Tw5JU0NUj3Jr4kzp7TMlMMePyHtQQwm%2B2B1gY6pgFrqxTT26cmTrMIh%2FpeSifmwOLZsQqGICjYINt0pyofPqlZVpUDKQuHwhdu50W1of0arXFKE3MKzWZsysovSq5WCrNCNRiSD2V2IJ9xPKwKFkSuu9yBm343DRL2%2BL9k8%2BLyZsdghImWd6G6fAME1clPqxa%2F8YvIMIFeLMAJlwFbsR9%2Fep36u%2BuUG0hE2vFPMAuRull%2BIx3iMXb%2B%2BkumkQ7PskhdetRl&X-Amz-Signature=a6c4b8de2f905a1d2e06a3a48ec11ddc65c94eec8ed0687787f15c895f031ef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624GMC3AV%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T061512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfkl009NaEEjQnmg0NJ9q%2Bup7ok4DIPz3d8%2F1S0fUKWAiBqfZsiairCzXzYuBkiBtEgeY35mg3H1Tae3OiJwJUI3iqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvUz6cXHQOfDj3TPvKtwDg%2Bsus9nu9uq5BKFjEqs7Bi8fL39pj3ELJv5oLnhncKjg1TSOfHxRRxHrZiBZrxLqF0KNN7fy7dEQdHBgk0bOBbg7QkASPSkykpZgeOZ%2Bs5vOcF5Q%2B64vShsLkRDZaNkXXMdYkdssA8cpRcVSN8yHTyvfxWgu4aDToxi0DEMNEryzbRioUJvn%2BeqVDFfYwsQyFCp3IXy0KkKyK%2FEGxuAhaaNF8XPDVEbYsuWeU9SwKY6wgdEclWPBZUNSz0%2Bt0SE1DM1dzZugGTXORcXbb2cEnKel99g1pr7xilqiBgULhJTtmiSOp5v550kPd6YkzrowBmNzD67KxR5a937Ti%2B83G0eWj6YNdBnULD4sgnJPV4EYdEQlUgdecykA%2FDRPpsbprl93e82Ct1m1vzWdjXUNQFX8E%2F8zloMsimI%2B5V4JsmFB5vqiycAm%2BZsuv94FYhYykPMSw83giiVeEfDBjibxhtozD0pbO3i4tzYbn2YZ677IL%2BUDaMZdkQ755QZEU%2FWfXrCF79zJlyuMZkHk3USxYiiTcGkYw56U%2FMwj9ds1dcBkRyZhb4PKE%2FBLjCUtZtdZ77NOLVTdd6YLwxrnxExgvYKDPll0q8Tw5JU0NUj3Jr4kzp7TMlMMePyHtQQwm%2B2B1gY6pgFrqxTT26cmTrMIh%2FpeSifmwOLZsQqGICjYINt0pyofPqlZVpUDKQuHwhdu50W1of0arXFKE3MKzWZsysovSq5WCrNCNRiSD2V2IJ9xPKwKFkSuu9yBm343DRL2%2BL9k8%2BLyZsdghImWd6G6fAME1clPqxa%2F8YvIMIFeLMAJlwFbsR9%2Fep36u%2BuUG0hE2vFPMAuRull%2BIx3iMXb%2B%2BkumkQ7PskhdetRl&X-Amz-Signature=37b40266d486ba424e60fa8c5ef6257c4cd8d9216ac6b3117a8bf0e1187fa1b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







