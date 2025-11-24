



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MX3STFH%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T182405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtpsep%2BmxvXLFoEjxs00QEXV2nzO8Q6qhQ6MEuQeWY%2BgIgByLmAbYPrytsIWSQcjxuCHeh%2BNXMBvur5TMBEIj7cm8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDBJ4o9xJZrOJvSLuLCrcA8twGPPM3ga2E8Lhc4osBGoRJ0AsG%2BfeOVJmesLYbo5JybCRvt2yVv8XKaBImC%2BGLWcLlq94tHsen6izH%2BRYErf5BdlP6DRVS0VOWpOykT6yw9Xe9uXMyGwGSQjiZa2wEjB5HSofOADt6ppmenxsmc%2BAKrIWuyY684aCtZE0r0Zex%2FgzBuxG86BjuvT%2Fx4SiySAtfcuoKnHzuHgvwzj28peA5QcpyoFxz5GKOVe7SxFHBLtLgx3r5CcBtwbl3XCq%2Fb2mpCaa0mrGsd87imWtsGVdwb3ZKniFkpLEXx2ZBBnFPJFa3gTfDhxaIRiPijMYH4dwJGcQYpvgFbXpMVzd9NPdCX3damXji5f43sGlcXvq4cnyQOKbaF5oPNZlRMCXGbk%2BW1c11SckVqZmYarqYg0JOHpBEvcTVL43cbIKHFYhtqWx72dujx91QXKYa3ixzXW5Z9WbMHN7vrmA%2BA6Lk%2BPdoUWMPlL1XGydzI1Uib0pjD2MH2JidMqVWTSgC8ycvdf%2FhW3s1llr%2BvsyUmZOx7AHenl%2BjIGXEC6qx%2FWyeHVycMfZRcar0mpSmE1FNpRisfDloTXn5uvu4bbDKoS%2Fcj%2FODRtQCpLjVf011%2F9rPTQSmyImtEkcfUkj0P3XMPyrkskGOqUBkr61wBqJVCEiK0%2F6xqRun%2FbYjL0xUfBTW00GAC5sIRuANgyogNRJA767gnSNwEtOPsY1PE8X1CQVWIKSQPRY9PG9rDdtdCf54jZlkazEneWHOI7PODTjzW8da26ulwNg3tYRn52orlp60ES29rnTAx7PMXclI0DiBGfkukopIfcRV8MNacNnNIJRWbvHf37FMjtpr0Sfqy8boWzMUzo64Ezx5H7l&X-Amz-Signature=ed561a2539af4968dfc3ea23004f45027b57a2ce2ca7c5891be2c1d2a3316382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MX3STFH%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T182405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtpsep%2BmxvXLFoEjxs00QEXV2nzO8Q6qhQ6MEuQeWY%2BgIgByLmAbYPrytsIWSQcjxuCHeh%2BNXMBvur5TMBEIj7cm8q%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDBJ4o9xJZrOJvSLuLCrcA8twGPPM3ga2E8Lhc4osBGoRJ0AsG%2BfeOVJmesLYbo5JybCRvt2yVv8XKaBImC%2BGLWcLlq94tHsen6izH%2BRYErf5BdlP6DRVS0VOWpOykT6yw9Xe9uXMyGwGSQjiZa2wEjB5HSofOADt6ppmenxsmc%2BAKrIWuyY684aCtZE0r0Zex%2FgzBuxG86BjuvT%2Fx4SiySAtfcuoKnHzuHgvwzj28peA5QcpyoFxz5GKOVe7SxFHBLtLgx3r5CcBtwbl3XCq%2Fb2mpCaa0mrGsd87imWtsGVdwb3ZKniFkpLEXx2ZBBnFPJFa3gTfDhxaIRiPijMYH4dwJGcQYpvgFbXpMVzd9NPdCX3damXji5f43sGlcXvq4cnyQOKbaF5oPNZlRMCXGbk%2BW1c11SckVqZmYarqYg0JOHpBEvcTVL43cbIKHFYhtqWx72dujx91QXKYa3ixzXW5Z9WbMHN7vrmA%2BA6Lk%2BPdoUWMPlL1XGydzI1Uib0pjD2MH2JidMqVWTSgC8ycvdf%2FhW3s1llr%2BvsyUmZOx7AHenl%2BjIGXEC6qx%2FWyeHVycMfZRcar0mpSmE1FNpRisfDloTXn5uvu4bbDKoS%2Fcj%2FODRtQCpLjVf011%2F9rPTQSmyImtEkcfUkj0P3XMPyrkskGOqUBkr61wBqJVCEiK0%2F6xqRun%2FbYjL0xUfBTW00GAC5sIRuANgyogNRJA767gnSNwEtOPsY1PE8X1CQVWIKSQPRY9PG9rDdtdCf54jZlkazEneWHOI7PODTjzW8da26ulwNg3tYRn52orlp60ES29rnTAx7PMXclI0DiBGfkukopIfcRV8MNacNnNIJRWbvHf37FMjtpr0Sfqy8boWzMUzo64Ezx5H7l&X-Amz-Signature=bac56707529492b7ff76b954d06448b432e62571782e17d3c459243e98206303&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







