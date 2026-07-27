



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVTQKIJI%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T093958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCTi83rUEtC3UI3O%2FxR2V4EEQoRPmQz6SBir92ZWXqAgIhAMQpn%2BeXEuJyRpe4kJ9Jc2ziHqQtkB%2BpnM7ZeBeucgKQKv8DCEoQABoMNjM3NDIzMTgzODA1IgyVJqWlPlTxHRmLsEUq3ANPcXBeJgHE%2BVr9R%2BFKSJtX6ecSgYW86XqibaWf7Vptnnj6DwEQRj3eWUtYr1ZL%2FoSur2iaemYyesRGIZZDkU%2BxNiQFjomtp5WqRRDEiH6SwBuI97HNz%2F0lb9VrhWJ5qtCpYFhmz5o6X0Die3sfs6opZ1BHR3HcBPvQa9%2BMhML1tD5rvWI5ShJbN9UT5b73KvCfpwOQZiZfFp0PLOQZqBzaCu1pOC%2Fr304JFk77J0zTG%2BuuHhhKQ0qsNLggyH135z9F%2BxKxc%2FdeuHp7AohLayc0C7EtRd%2FdLQHX3uENfCkbpgFCZj8xRREsEoZ%2F5LDRBu9ID8F%2B6zhSl%2FZPehE483u0FBUehDzpmaRJq38yokb903RKr97%2BcS7OinYQVrMpZ%2F74Ph7zwZi9iEriE8epxSXKHtrQccf%2F2J1jcSLyTPzBkmxlvXCMhi6f4u1LPj1loo2DEd9heCkXSiMjigkd9TJqMpDulSi4LaZNjaFktNks0Fdz8e5aboyDJl1OmP09ykcIxg2d%2BmyWz7v8d3aU4Uynu62RN4kGvrFTwZxTTP3v7HOsTYi6CJ9%2FpW5ni1Je%2Fw1HPYS0UkWAUKGkmYM0SG%2B5hIU0WCo%2B%2FrBVbhCxQttETc36bP8sN15i9YQ8HTDHs5zTBjqkARWAh4CQPwiqggxHgjrkukrNK%2BPsvrKStIIDg6fNiTSxNSp0pSkq20rKnHbdFlM6%2Be4saQOwGWTeDu3keqYTb3MukbSJaK0i1yuagVa1GcRDshZtaSkvR%2BIq9R7zj%2BDk41%2BSCXbU656pf5Ef724GDChugrR%2FLkU%2F7WbPvMIQtZE2ies%2FVeRkw8O9gUIHcRShYxuhE0wvuINq4aREHW%2BuqloJY4yV&X-Amz-Signature=20e85d8e84aa084362c25473b93c9d0f76ab59de02ae9f81f1e7065296eb6e65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVTQKIJI%2F20260727%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260727T093959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCTi83rUEtC3UI3O%2FxR2V4EEQoRPmQz6SBir92ZWXqAgIhAMQpn%2BeXEuJyRpe4kJ9Jc2ziHqQtkB%2BpnM7ZeBeucgKQKv8DCEoQABoMNjM3NDIzMTgzODA1IgyVJqWlPlTxHRmLsEUq3ANPcXBeJgHE%2BVr9R%2BFKSJtX6ecSgYW86XqibaWf7Vptnnj6DwEQRj3eWUtYr1ZL%2FoSur2iaemYyesRGIZZDkU%2BxNiQFjomtp5WqRRDEiH6SwBuI97HNz%2F0lb9VrhWJ5qtCpYFhmz5o6X0Die3sfs6opZ1BHR3HcBPvQa9%2BMhML1tD5rvWI5ShJbN9UT5b73KvCfpwOQZiZfFp0PLOQZqBzaCu1pOC%2Fr304JFk77J0zTG%2BuuHhhKQ0qsNLggyH135z9F%2BxKxc%2FdeuHp7AohLayc0C7EtRd%2FdLQHX3uENfCkbpgFCZj8xRREsEoZ%2F5LDRBu9ID8F%2B6zhSl%2FZPehE483u0FBUehDzpmaRJq38yokb903RKr97%2BcS7OinYQVrMpZ%2F74Ph7zwZi9iEriE8epxSXKHtrQccf%2F2J1jcSLyTPzBkmxlvXCMhi6f4u1LPj1loo2DEd9heCkXSiMjigkd9TJqMpDulSi4LaZNjaFktNks0Fdz8e5aboyDJl1OmP09ykcIxg2d%2BmyWz7v8d3aU4Uynu62RN4kGvrFTwZxTTP3v7HOsTYi6CJ9%2FpW5ni1Je%2Fw1HPYS0UkWAUKGkmYM0SG%2B5hIU0WCo%2B%2FrBVbhCxQttETc36bP8sN15i9YQ8HTDHs5zTBjqkARWAh4CQPwiqggxHgjrkukrNK%2BPsvrKStIIDg6fNiTSxNSp0pSkq20rKnHbdFlM6%2Be4saQOwGWTeDu3keqYTb3MukbSJaK0i1yuagVa1GcRDshZtaSkvR%2BIq9R7zj%2BDk41%2BSCXbU656pf5Ef724GDChugrR%2FLkU%2F7WbPvMIQtZE2ies%2FVeRkw8O9gUIHcRShYxuhE0wvuINq4aREHW%2BuqloJY4yV&X-Amz-Signature=07c6f78c5620acbe6fe7d8f1bed09e651b68d993327af10b7e560af7fec26cb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







