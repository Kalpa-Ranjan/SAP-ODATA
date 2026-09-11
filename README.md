



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUA5G3AE%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T061245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC1XvnmjkLnL0xUFhFOVhFPdrTglsPBQTtTNLjxO%2FYz4AiEA3Iz%2BbMAy1BhUky9Xqd72n1HHfsurK1iUmxnxNba%2F9PIqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGI2cz3W2xXMNaI1ircAyVlzgjgfOrM2rWV4plee8St%2B6fzDjBU7lWtgqXT4bgyUmYJbsalU3Vmc80pHeKFZ%2BFb3GS8eCPlh6Sbpr3uRw7kCyqIe5nw3xBROAbBgDN1WKymvgfw3VrglK95%2BVdxo3gvWVZOHGRKYJFjPNOM5L7R8e33XSGTb%2B22GAz01iRFaNBC2XYad8u8aLfL9ArLYmqdgVrjhAvdjANfcbAYgST%2FgL7OMv4FBpVODCYu1BYUpXp9wrl3uHQzA0E8keQjN1U1romO94Tn8n2O0DYYQ%2Ba%2FEsvVuroj8gxr%2FvwhDc%2B%2B6zVSmGWBr7aLgYyTMGCrKjPks2NguvEn8KZLPqtWeRBhp6AOMoF8fq%2FDjwfYJV7ZFTnCRAeWJtrC5NUCNRJISaWaJb4MsdWfIroUxgYsWGtQTq4Z8I3n24VcIlGSmrly4hAmK8XWTgXlZqbJgIBN6TGzDINB3YqHr8eVraOjyhzj23wbOB5hZQIKH3TRqFYTkbc6y8muR3HS4rHHOIm%2BTFdWD84SsQRBTyxyLVeoI1odI8txyLEcr9YXDgPtGuw%2BlOkKZLgwhuRIyPyRseKCKfbzgPq9LhNNvwc0LzhYQFOhVJ9t5PQ6k22PY387J%2BttesIMkTF0Lmy5iYB9MOiWjtUGOqUBGP%2BFENcrhmXsA4VLKUAEP7Ts6SypKFg64dKizljIxeMqpCBF8wp8fAdkL80kiY0dbc8DR8hLkCLka6PS0onZ3NlXZuEu13s745umwB1ugBNl2w%2Bw%2BhtCJxBgQ5bg0IjAOIoWACFRgsDXrQLfuUuhIw5NueLaUX60EVX%2FXrzvbb8alAaM6gkgXbm47y%2BYR4az2oMoEjkrzBdhGhsZ3y%2FAH6LUadLi&X-Amz-Signature=076693aeb1b244a6bf643f094415a7bc85b97fc7f0b0a9e74640cd4cd0e4ce73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUA5G3AE%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T061245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC1XvnmjkLnL0xUFhFOVhFPdrTglsPBQTtTNLjxO%2FYz4AiEA3Iz%2BbMAy1BhUky9Xqd72n1HHfsurK1iUmxnxNba%2F9PIqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGI2cz3W2xXMNaI1ircAyVlzgjgfOrM2rWV4plee8St%2B6fzDjBU7lWtgqXT4bgyUmYJbsalU3Vmc80pHeKFZ%2BFb3GS8eCPlh6Sbpr3uRw7kCyqIe5nw3xBROAbBgDN1WKymvgfw3VrglK95%2BVdxo3gvWVZOHGRKYJFjPNOM5L7R8e33XSGTb%2B22GAz01iRFaNBC2XYad8u8aLfL9ArLYmqdgVrjhAvdjANfcbAYgST%2FgL7OMv4FBpVODCYu1BYUpXp9wrl3uHQzA0E8keQjN1U1romO94Tn8n2O0DYYQ%2Ba%2FEsvVuroj8gxr%2FvwhDc%2B%2B6zVSmGWBr7aLgYyTMGCrKjPks2NguvEn8KZLPqtWeRBhp6AOMoF8fq%2FDjwfYJV7ZFTnCRAeWJtrC5NUCNRJISaWaJb4MsdWfIroUxgYsWGtQTq4Z8I3n24VcIlGSmrly4hAmK8XWTgXlZqbJgIBN6TGzDINB3YqHr8eVraOjyhzj23wbOB5hZQIKH3TRqFYTkbc6y8muR3HS4rHHOIm%2BTFdWD84SsQRBTyxyLVeoI1odI8txyLEcr9YXDgPtGuw%2BlOkKZLgwhuRIyPyRseKCKfbzgPq9LhNNvwc0LzhYQFOhVJ9t5PQ6k22PY387J%2BttesIMkTF0Lmy5iYB9MOiWjtUGOqUBGP%2BFENcrhmXsA4VLKUAEP7Ts6SypKFg64dKizljIxeMqpCBF8wp8fAdkL80kiY0dbc8DR8hLkCLka6PS0onZ3NlXZuEu13s745umwB1ugBNl2w%2Bw%2BhtCJxBgQ5bg0IjAOIoWACFRgsDXrQLfuUuhIw5NueLaUX60EVX%2FXrzvbb8alAaM6gkgXbm47y%2BYR4az2oMoEjkrzBdhGhsZ3y%2FAH6LUadLi&X-Amz-Signature=5e497bf9e361f0edb51424bf2890ab8b247e10f696153f4034b2f0bfe6104dbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







