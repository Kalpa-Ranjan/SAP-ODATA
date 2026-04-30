



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUECGW7M%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T134400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2Bt%2FQ6KWUDcRToUv1x5%2BcHkvL2wuANJQzGNErp3O1q1AiEAz%2FeO3gup9z5oCDHbcS0Tip5Pen0Yx4K1aaQ5a8hmSoAq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDKhD6pCdDkEnrRO0kyrcA5E3s%2BgK7xrTvuqcjkzI%2FP%2B9ohoVdaMJmoZk1fY5zrO4HeeeiyTC2uILGZyZ%2BdRnEMQmZp5Io%2FhjwIJXULCDzVAY8H%2Fggn8ZkVojuhz2sqVD8uHDpOBrBgJSEg8Aj2T%2BnEhXLI6kmjkhUGrJam5CA85frsn3ptZNU62EAuwABZ%2BbHJth2gVEjUKoMpbzyqpPCjXda97Wd9XLhIGzsXk1MWw2DpPsCz7km4aJ3O43NWwY3yUZewqMEFdwHUWJ%2BUJy0kwQzcZMLsV9UBdw78%2Fy7m0MWYFazOUSMuzPRrUq6xVCYzejcKhi52LvN6tSVDvQOJQW24fIvBg1D%2FH7WW%2BR4CmMPql0wHzvX91KNwL8oLhSYvJgroPs9vRY3CuzdEppYWrruevbzKgphOo52Fj9cuDWm%2FzM76Ih9YnwbguPK65dJqgNsCsQY8AxfQx7FplZrR9y8pad8SxEWbHQ6hWBc7PRIAMtWkQSIbO9eJIQh7D9q2kVFGjZhz368uBrRB%2FJefzaIoDq2V%2BIqkV4VvWvhOQCcb3QpH9SaqkwBrDozKZMGi103Lbm%2FGvvloJefCcRAXPcWX0j%2BE%2FsDQMYIDQJyMSwSD5flzadsvtOwfx4NsZ5yIwwc6%2Feuj9Y04MUMNCuzc8GOqUBo%2BJCSEDoEAGNuU5dbi4pqmKFlTWzJlrwhU1DOBb5KuT%2F%2B8UFgR8rDFpt7TwgaC2fHC2NzBXuB6HrUiZvoeqQuWcZeoPysB29dZkknWMbR3XuvXL0%2F%2BExMiDcgCZ6oZ0%2Be%2F17uTnJwa2lzIgwbZoez%2BSjRvZpu4h91%2FwY5ZTz605TEEM7sRFYisSY2vTajfQ2saiBw%2F90T6%2Bo%2BZZKhGqXAe8FS6lD&X-Amz-Signature=3bfe16c20057679cb6d603f90ba6ae118aeee128c1d300a1508fb81e068d961b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUECGW7M%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T134400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIB%2Bt%2FQ6KWUDcRToUv1x5%2BcHkvL2wuANJQzGNErp3O1q1AiEAz%2FeO3gup9z5oCDHbcS0Tip5Pen0Yx4K1aaQ5a8hmSoAq%2FwMIDhAAGgw2Mzc0MjMxODM4MDUiDKhD6pCdDkEnrRO0kyrcA5E3s%2BgK7xrTvuqcjkzI%2FP%2B9ohoVdaMJmoZk1fY5zrO4HeeeiyTC2uILGZyZ%2BdRnEMQmZp5Io%2FhjwIJXULCDzVAY8H%2Fggn8ZkVojuhz2sqVD8uHDpOBrBgJSEg8Aj2T%2BnEhXLI6kmjkhUGrJam5CA85frsn3ptZNU62EAuwABZ%2BbHJth2gVEjUKoMpbzyqpPCjXda97Wd9XLhIGzsXk1MWw2DpPsCz7km4aJ3O43NWwY3yUZewqMEFdwHUWJ%2BUJy0kwQzcZMLsV9UBdw78%2Fy7m0MWYFazOUSMuzPRrUq6xVCYzejcKhi52LvN6tSVDvQOJQW24fIvBg1D%2FH7WW%2BR4CmMPql0wHzvX91KNwL8oLhSYvJgroPs9vRY3CuzdEppYWrruevbzKgphOo52Fj9cuDWm%2FzM76Ih9YnwbguPK65dJqgNsCsQY8AxfQx7FplZrR9y8pad8SxEWbHQ6hWBc7PRIAMtWkQSIbO9eJIQh7D9q2kVFGjZhz368uBrRB%2FJefzaIoDq2V%2BIqkV4VvWvhOQCcb3QpH9SaqkwBrDozKZMGi103Lbm%2FGvvloJefCcRAXPcWX0j%2BE%2FsDQMYIDQJyMSwSD5flzadsvtOwfx4NsZ5yIwwc6%2Feuj9Y04MUMNCuzc8GOqUBo%2BJCSEDoEAGNuU5dbi4pqmKFlTWzJlrwhU1DOBb5KuT%2F%2B8UFgR8rDFpt7TwgaC2fHC2NzBXuB6HrUiZvoeqQuWcZeoPysB29dZkknWMbR3XuvXL0%2F%2BExMiDcgCZ6oZ0%2Be%2F17uTnJwa2lzIgwbZoez%2BSjRvZpu4h91%2FwY5ZTz605TEEM7sRFYisSY2vTajfQ2saiBw%2F90T6%2Bo%2BZZKhGqXAe8FS6lD&X-Amz-Signature=fbb06488c7721c16ad979e19cd93bec306c8bb8c74d1c8b0349181ecca0ed840&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







