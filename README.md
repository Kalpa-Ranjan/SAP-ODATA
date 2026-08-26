



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HWRMFDS%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T005816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIAj4E7TjcE9mIh5pzDvBA7x2hmXkbb968m5j249uyvuyAiEAnZRH0xFSzT6PI4jUd%2FO1ctIAf%2B1iAVl3LWpciVlMlGgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLGR9bl8k5Z3jHKTDCrcA7f5QR4EEXc9JRYZIkYgUqgKwBldDuhuY4G%2FxBu%2F%2BcqAqJe4YgRZzLcbW3jvEDfhrxKYqysrpvnoH3pfCX0futQw%2BKlVNEu6%2Bj%2Bp%2BaA%2FbohKSjxAsdm277sHjCX1U7XIKoMUGzH1xBERc%2BIPXmCSXiQnOCmckI842nbswESKaHai%2Fh0xyiWzTGWz7j9N3LB5n%2FZ36s6OnKctnfcdJdczJoyyDLmrQXbHpAeLe6DJRpfTrdKaMOxVx00%2FKrvKL8Z1znfH4wppvDzqwyAcRY2ow67TXUB%2Bvg4Ng4QqhMalj6xw5Bp9UxrZFmd2B%2F134anW1PuaEMkOuZX0k%2BVavjaiNrEloaZRjQ20gvA%2F2dyXKJXaHc%2FyLoWP2TFAmrWDR9Ib838%2FdP59JZq5KYu5w3bwel1n6B6XEwPBjDvKzJmIOt97bBmVe9OxJw6iGETFMW1N19taZuSo8aOl0OaF5wPP9JMfZnS%2F7bR0VMWfkRF3uve0iNMDD%2F8sf8Hfm4NOk3r%2FxJ%2FvAJ5CowM58%2FeBxl393kpX%2BZHyCrQp1rgV4TEZzjXNB9SHEglA4Spl%2FDRbEOEh7PXPbnYh1izPuIoujL1vwuN%2Fkga83BZP8rRCW3N384r%2Bvm9o9Qi04xecAxgWMMTYuNQGOqUBqMrFJwElSt76hFUWy69X0xRXVK5xnWZxODQsPOnltsfq17Ep79AB97SPSS496uzQ9jM%2F1AVyv6ARnOd3VRl1gAEeUYatduIat%2B7LofWAv7Az%2BYaSrm3QwEV2MVjkZgyQJqaltGGPUrNnQezHA5DT4fYPYk9SXGR8fIppJ1d%2B2LarCmrJ2C%2B69dIWFc2XI3T05tWQjCFvHDnd6Ih7UUTSUeVWd2lq&X-Amz-Signature=b3e5df2f0ef912a69c93e2983ec2157a0f050f801ab1a05286cea2386d433bfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HWRMFDS%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T005816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIAj4E7TjcE9mIh5pzDvBA7x2hmXkbb968m5j249uyvuyAiEAnZRH0xFSzT6PI4jUd%2FO1ctIAf%2B1iAVl3LWpciVlMlGgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLGR9bl8k5Z3jHKTDCrcA7f5QR4EEXc9JRYZIkYgUqgKwBldDuhuY4G%2FxBu%2F%2BcqAqJe4YgRZzLcbW3jvEDfhrxKYqysrpvnoH3pfCX0futQw%2BKlVNEu6%2Bj%2Bp%2BaA%2FbohKSjxAsdm277sHjCX1U7XIKoMUGzH1xBERc%2BIPXmCSXiQnOCmckI842nbswESKaHai%2Fh0xyiWzTGWz7j9N3LB5n%2FZ36s6OnKctnfcdJdczJoyyDLmrQXbHpAeLe6DJRpfTrdKaMOxVx00%2FKrvKL8Z1znfH4wppvDzqwyAcRY2ow67TXUB%2Bvg4Ng4QqhMalj6xw5Bp9UxrZFmd2B%2F134anW1PuaEMkOuZX0k%2BVavjaiNrEloaZRjQ20gvA%2F2dyXKJXaHc%2FyLoWP2TFAmrWDR9Ib838%2FdP59JZq5KYu5w3bwel1n6B6XEwPBjDvKzJmIOt97bBmVe9OxJw6iGETFMW1N19taZuSo8aOl0OaF5wPP9JMfZnS%2F7bR0VMWfkRF3uve0iNMDD%2F8sf8Hfm4NOk3r%2FxJ%2FvAJ5CowM58%2FeBxl393kpX%2BZHyCrQp1rgV4TEZzjXNB9SHEglA4Spl%2FDRbEOEh7PXPbnYh1izPuIoujL1vwuN%2Fkga83BZP8rRCW3N384r%2Bvm9o9Qi04xecAxgWMMTYuNQGOqUBqMrFJwElSt76hFUWy69X0xRXVK5xnWZxODQsPOnltsfq17Ep79AB97SPSS496uzQ9jM%2F1AVyv6ARnOd3VRl1gAEeUYatduIat%2B7LofWAv7Az%2BYaSrm3QwEV2MVjkZgyQJqaltGGPUrNnQezHA5DT4fYPYk9SXGR8fIppJ1d%2B2LarCmrJ2C%2B69dIWFc2XI3T05tWQjCFvHDnd6Ih7UUTSUeVWd2lq&X-Amz-Signature=e8b1f722fa44e5c03b5441678338d495bfb727818e7b0125ce736f343d291753&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







