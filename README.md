



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5VTGUWL%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T114316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIArh6K3cmDEbLV3tcyM6CMt9oJqlu0%2Fzzx2TzQLk8kluAiEA%2FYAiXEQ%2FniwZLS6G0Wmw5LBhirUgLEfcHSNm%2BV%2FfBsEq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDACFpOEKEKtiQ2AULSrcAzj3XQF56z2wpWQkcQLEnu5cedJpOeBDrQAjZai2uiUbCg0IIsUmnavB0rcPn%2FNWtdafcZSWln2katxxXn2B8jo0uNGgf3PexGq3rgYJHoDmC1aHaxdijViM1GNsPn4PHUa3DfTSVsdQhumFwMsqurX3gR8dqJ6MQOLd1TwMWteVSy44TAc5yv4wrpqChmnsglUiZts7ld8SMIUPrwHpmfKzMM%2Fc4I7b09%2FM3XiMTicHU0lDjx6y6p8vi8Gxg7az%2FFKVhLS81NUklD1E1lPRtd6a2f8lXd%2BQ9dbvd4rovDdivOU5q0nvGQxgqJbor2Ufx0WxqqD6naYuum6kwGBoKdfSyIQCp8FTuBZJXBrHVAJ7cBmBDXBO19XsIwjwnSeGobYOrY0IurnzV8fODfJqleIPLTvlpAOWbD2gb9C75vTej9wsh%2BBJx4qJ%2BmQRzJNj5J4JKB8NT0gleAmrAXOsLneyWu3fN9Kcq6OGuusUXeTQL9LwfRlaxkPmr49pPJw%2B1ha39Ww1Euq5vtyTSFqpNVWEz8%2B11rsejcCfSjSpncTw3vQZCKwgIpuqUVuEwHqVAoYonUgRJEWQtOmCgq0puwNg2dHdTNec3tjWB3Q6pIY1gDOWvl%2FgvRxnd6zxMIOh5NEGOqUB%2FFvsWMh2SKEwJMZBXgsiXBaoJSahv0YHanw8XEYNBH9EH6XwX5uc%2Fe%2FXZBsTnXT8BgznOBJgyOHOTx4Z2y4Lg%2Fcoww3f6Vf3W733BfvzA5IawS8wOtIpjC%2Fu3N%2Bjza7KMKs%2BvyWKfIv%2Fqbz9OMfJaINfIF8kuuObz4iGXJnPVGZyttxB8NXyMvNjAiy6rAjp2YC3NnNTHOzv49o6waTQRNsPrT8P&X-Amz-Signature=28b95f2904280c8b27c3b77b22b9fda2e1971d1c36d356f257491348c4e54fdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5VTGUWL%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T114317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIArh6K3cmDEbLV3tcyM6CMt9oJqlu0%2Fzzx2TzQLk8kluAiEA%2FYAiXEQ%2FniwZLS6G0Wmw5LBhirUgLEfcHSNm%2BV%2FfBsEq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDACFpOEKEKtiQ2AULSrcAzj3XQF56z2wpWQkcQLEnu5cedJpOeBDrQAjZai2uiUbCg0IIsUmnavB0rcPn%2FNWtdafcZSWln2katxxXn2B8jo0uNGgf3PexGq3rgYJHoDmC1aHaxdijViM1GNsPn4PHUa3DfTSVsdQhumFwMsqurX3gR8dqJ6MQOLd1TwMWteVSy44TAc5yv4wrpqChmnsglUiZts7ld8SMIUPrwHpmfKzMM%2Fc4I7b09%2FM3XiMTicHU0lDjx6y6p8vi8Gxg7az%2FFKVhLS81NUklD1E1lPRtd6a2f8lXd%2BQ9dbvd4rovDdivOU5q0nvGQxgqJbor2Ufx0WxqqD6naYuum6kwGBoKdfSyIQCp8FTuBZJXBrHVAJ7cBmBDXBO19XsIwjwnSeGobYOrY0IurnzV8fODfJqleIPLTvlpAOWbD2gb9C75vTej9wsh%2BBJx4qJ%2BmQRzJNj5J4JKB8NT0gleAmrAXOsLneyWu3fN9Kcq6OGuusUXeTQL9LwfRlaxkPmr49pPJw%2B1ha39Ww1Euq5vtyTSFqpNVWEz8%2B11rsejcCfSjSpncTw3vQZCKwgIpuqUVuEwHqVAoYonUgRJEWQtOmCgq0puwNg2dHdTNec3tjWB3Q6pIY1gDOWvl%2FgvRxnd6zxMIOh5NEGOqUB%2FFvsWMh2SKEwJMZBXgsiXBaoJSahv0YHanw8XEYNBH9EH6XwX5uc%2Fe%2FXZBsTnXT8BgznOBJgyOHOTx4Z2y4Lg%2Fcoww3f6Vf3W733BfvzA5IawS8wOtIpjC%2Fu3N%2Bjza7KMKs%2BvyWKfIv%2Fqbz9OMfJaINfIF8kuuObz4iGXJnPVGZyttxB8NXyMvNjAiy6rAjp2YC3NnNTHOzv49o6waTQRNsPrT8P&X-Amz-Signature=396e405208e4fdc37bcc290aa89ac29366c8d7e5a00e9c0ee2e2f321c74d03bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







