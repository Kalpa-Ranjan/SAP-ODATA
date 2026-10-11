



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJP7AFRQ%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T121149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2GYpxhGMyFAOKNGkP7S178AgR8w%2Fj5apA7Kfo29Fm2AIgCISN5hr8w6%2F7h1t8Q3lNhjnIfrWJ%2F0Ff06YiNwkn0Msq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDL%2F5qkN%2Boc4TvdaqgircAxz0zEvyuMdb%2FgjI00f%2FkGiTqClrcaCbdOxYBYIvbkuEtbKMIJx2U5QdYJEmDwTrVVdx9lKbLbWkCpFiM9Aeiz%2Fwgiqek8hh%2FWaGAoKEWsSF0DDBEAb3VSzH%2BkcWn2pCbCSkJedt4zvx2gjnNvlDGgZnUwcCTs3P%2FsVJsnfu1EZdO0O6gGFQY%2BF%2Brrf8OfKy%2BQ3GQ%2FE%2FwQshDt55GEtLEAYXmCCzeGWJHsJFHKMredmS7v85NxKoBHwEoSdBxpWJqICab%2BWm4Az2UkE5SHDLX6Y3GrtpuRoBtEV%2FyDc9mUHgmCHktEXns4AI7dtcIll%2BPWtzGxMHapErhrVJbjUiGdrr5mq4%2F5C4tHC14DLfSW4w%2Bt1vagrtyTcO1b7UBoY%2FGr26IiZxbevI8MTp0cAjgN0hbJgNV1hmP8z866lEcBtdnmDsXJWMgu8LwjLhs%2BH%2Fdg4ZwhJ6htCImvqLtTff6D3BC81N3zzeRbNxDrbv82t7yUs4NlVtV9XhXEAV8igUsC1wvKdfl1hwIwjeTTyqGc8H0SU2UhrMZde0W1AktF86WDTeVuqIgCU1Ad4AU6MQfb6dFN9M1Q33H5nG28GqC9SoyIw%2Fg%2FohmzBtLU0IdBESIolJsqTIYsO%2FMGATMNfUrdYGOqUBUdrjhLqkqP%2BXStdZvfqHm20fGeWRt2j8Yb72%2F%2F4MYrvRjzuJfDGO2OjKhCf004MThfaHZyoK61kkqn17pWACJgaJiT3VWD0lus%2BYUFpTYsrv1EcLhW3PFl2g8PqzVpMzfm%2F6hMPthBgaKCdtz3iZ%2B1GrEt5XMqjad8c4dAuPabW80kleR5jfhjyNqqEdoqrCZNGMLYCBthIemcRxLGaKXo%2FuYWQV&X-Amz-Signature=e549b68ab7484e57803f4eedcd658ab571527b4d888553fd6c06554ab7888dab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJP7AFRQ%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T121149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2GYpxhGMyFAOKNGkP7S178AgR8w%2Fj5apA7Kfo29Fm2AIgCISN5hr8w6%2F7h1t8Q3lNhjnIfrWJ%2F0Ff06YiNwkn0Msq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDL%2F5qkN%2Boc4TvdaqgircAxz0zEvyuMdb%2FgjI00f%2FkGiTqClrcaCbdOxYBYIvbkuEtbKMIJx2U5QdYJEmDwTrVVdx9lKbLbWkCpFiM9Aeiz%2Fwgiqek8hh%2FWaGAoKEWsSF0DDBEAb3VSzH%2BkcWn2pCbCSkJedt4zvx2gjnNvlDGgZnUwcCTs3P%2FsVJsnfu1EZdO0O6gGFQY%2BF%2Brrf8OfKy%2BQ3GQ%2FE%2FwQshDt55GEtLEAYXmCCzeGWJHsJFHKMredmS7v85NxKoBHwEoSdBxpWJqICab%2BWm4Az2UkE5SHDLX6Y3GrtpuRoBtEV%2FyDc9mUHgmCHktEXns4AI7dtcIll%2BPWtzGxMHapErhrVJbjUiGdrr5mq4%2F5C4tHC14DLfSW4w%2Bt1vagrtyTcO1b7UBoY%2FGr26IiZxbevI8MTp0cAjgN0hbJgNV1hmP8z866lEcBtdnmDsXJWMgu8LwjLhs%2BH%2Fdg4ZwhJ6htCImvqLtTff6D3BC81N3zzeRbNxDrbv82t7yUs4NlVtV9XhXEAV8igUsC1wvKdfl1hwIwjeTTyqGc8H0SU2UhrMZde0W1AktF86WDTeVuqIgCU1Ad4AU6MQfb6dFN9M1Q33H5nG28GqC9SoyIw%2Fg%2FohmzBtLU0IdBESIolJsqTIYsO%2FMGATMNfUrdYGOqUBUdrjhLqkqP%2BXStdZvfqHm20fGeWRt2j8Yb72%2F%2F4MYrvRjzuJfDGO2OjKhCf004MThfaHZyoK61kkqn17pWACJgaJiT3VWD0lus%2BYUFpTYsrv1EcLhW3PFl2g8PqzVpMzfm%2F6hMPthBgaKCdtz3iZ%2B1GrEt5XMqjad8c4dAuPabW80kleR5jfhjyNqqEdoqrCZNGMLYCBthIemcRxLGaKXo%2FuYWQV&X-Amz-Signature=ab46d42a1b94115fbd30dc9a723d3e0e0f4e2cb42a39a764323bab47d3661c80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







