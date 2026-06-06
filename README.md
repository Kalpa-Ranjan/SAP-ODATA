



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTBWIE3G%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T191330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKps77wHZ3gLYHmv6hKLJNZnh8ShC%2BaVzeUVf5XwclcAiEAjSgu%2BBDGqnhjPXL%2FO1%2BVp2CUU9lupf%2Bx6Rm5NDICHU8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtgoJTQG18QGz8xOSrcA4ytoqTQSDTzxwLisIbAHQFoALliE%2BYyfOs%2FOQDD4wRXDGXKoHJKCfnuaZOzfzT6OcSpFQln1R1WQc32Q5TNwkLHAt%2FqUjI5zVTGOjKummyezvwTRB1CJnxf4z3fG5dxE6udzvTEomWytZSf%2FWcIbWxGsdPeaGgfimCB2iY9dHH2wpQpljk0PEES0fYNYZ1jEkWUnE%2BUDpMMuKXe9WWJNmoijwWsZm5fhZ%2BKhBnICN7yr2Lc677KrRgZB6094eozXRoy0Kqo4zCU5kSI60fuI35f%2FlCLXvaX2oVulidodVz%2FyvvWYq0IkukQ6GqMG6Qe9VVfFITJ3u5axKirXu1AOZXJ5ops7%2FBG82tUqgx6ifGpfK1bLkzratriQHwIN668MZkuuGe39gLe8BTQrq7Q1bU9OVFI5rSxfkPmvhc0bIVOvpvCcbF7fceK05B9tUAW3fcqrNI%2BLvTHrixNiuo7XZPvgrTGIARPv%2BKQbLKxdkOYsnTm9709tAEZTyDeWJ1sFPiZolj3SDItsz7FQK9Axgc40hlbj6Ch%2FzvBsdU2oTmWhceD57lQ4pwh8N34I%2BBRFmhkXGTJAJUUBXy3j8WvsTKNdBfMZLWWgOv0wQxGoH%2B%2FUG0WyAjf%2Fm%2Fvxok6MJrEkdEGOqUBV6TuuvDCpiP9I8kcsaezb9yDSiZNQlvR5n3avtlPyOAGil3NrS7fccwqOnP8Wzdoq0e1zHHw0hwg7JI7ON1nyNYOGcYuxdbeWbsgV0ubn0SiT9NL9vR15hD4z9Ct1RDi67qZ%2BB9heR8AUUKxYftOSk0M1LyOU1DoNh8m6%2F37WFhLevKRYSy6%2BAvR9cAzkGNCXDvAsK4cOI9oV0GhHiN%2BKQ99IOef&X-Amz-Signature=146c08edf985aee156e802645aee95c2e706a6009f8ead6ffbf6d11a1d0b8738&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTBWIE3G%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T191330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEKps77wHZ3gLYHmv6hKLJNZnh8ShC%2BaVzeUVf5XwclcAiEAjSgu%2BBDGqnhjPXL%2FO1%2BVp2CUU9lupf%2Bx6Rm5NDICHU8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtgoJTQG18QGz8xOSrcA4ytoqTQSDTzxwLisIbAHQFoALliE%2BYyfOs%2FOQDD4wRXDGXKoHJKCfnuaZOzfzT6OcSpFQln1R1WQc32Q5TNwkLHAt%2FqUjI5zVTGOjKummyezvwTRB1CJnxf4z3fG5dxE6udzvTEomWytZSf%2FWcIbWxGsdPeaGgfimCB2iY9dHH2wpQpljk0PEES0fYNYZ1jEkWUnE%2BUDpMMuKXe9WWJNmoijwWsZm5fhZ%2BKhBnICN7yr2Lc677KrRgZB6094eozXRoy0Kqo4zCU5kSI60fuI35f%2FlCLXvaX2oVulidodVz%2FyvvWYq0IkukQ6GqMG6Qe9VVfFITJ3u5axKirXu1AOZXJ5ops7%2FBG82tUqgx6ifGpfK1bLkzratriQHwIN668MZkuuGe39gLe8BTQrq7Q1bU9OVFI5rSxfkPmvhc0bIVOvpvCcbF7fceK05B9tUAW3fcqrNI%2BLvTHrixNiuo7XZPvgrTGIARPv%2BKQbLKxdkOYsnTm9709tAEZTyDeWJ1sFPiZolj3SDItsz7FQK9Axgc40hlbj6Ch%2FzvBsdU2oTmWhceD57lQ4pwh8N34I%2BBRFmhkXGTJAJUUBXy3j8WvsTKNdBfMZLWWgOv0wQxGoH%2B%2FUG0WyAjf%2Fm%2Fvxok6MJrEkdEGOqUBV6TuuvDCpiP9I8kcsaezb9yDSiZNQlvR5n3avtlPyOAGil3NrS7fccwqOnP8Wzdoq0e1zHHw0hwg7JI7ON1nyNYOGcYuxdbeWbsgV0ubn0SiT9NL9vR15hD4z9Ct1RDi67qZ%2BB9heR8AUUKxYftOSk0M1LyOU1DoNh8m6%2F37WFhLevKRYSy6%2BAvR9cAzkGNCXDvAsK4cOI9oV0GhHiN%2BKQ99IOef&X-Amz-Signature=9995b82b325b2cc5f191003e428b1aeedb9291d779561bcc1fabb715511edbe0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







