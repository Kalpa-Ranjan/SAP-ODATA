



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635ELQFKL%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T185458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCIwp7cs1GkMh%2FYb8rRxAUjd15eWPHSiO28mTN%2FVXLyNwIhAN%2Fu%2B4BOP3hMz32TF3SAqbi%2F3g37ExJ70XFsQlCe0XTGKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FkECNKFTgVUFBZhoq3ANk6z9P%2B3AP%2F%2FP07iJHhl2hRhLAleBcsbGOz8M9ld3yeTpmA5sMXKjTGEf%2FIZLmXWucuIYl7I%2FcuQn%2FraJRtLpZ2yomRpfrNgHiLGoiXXMJlugiTWVeWumpCmAogQfpiLCgymRyhYhMboq%2BWkYenxuulQJesdmFhGwlYbgziRRuAQiWZkwcQrXkSwSMplGxMFIYXoL78ZTncEmT5F2N3ne67zD2Ti1VOft9VVioMZnVbZ2x2yJQSesmxP84O5peF3ims53EJ2wnVzsx2vAubqXhy38%2B0wCUiGsbCEQaxMQmVVpSx4MjjiZjzmDoLXI%2FlZ%2BGBq7w4R%2B8%2B9UwlikVaesO1M0Tkj%2FEiEw%2FAh0PmxgP3DOfd3pJN15pIdBit2H37IGjOOiB2R9A%2FHWb2ywvb09N%2FAwFqK1UkMxz%2FlFSwthgg3e6uj7PJ4JK8%2FyoNUEWpPBw7M5xKNG3oYPUa3W80%2BpqWcBdLYhZ6jVfRVh%2FE2DEtYKvsVLQC%2FYtZ2Ig8gZeq5Tbt0si4176nwi6A3ZgLS8j46XRcrR7R2aoBFbtN6doJziIm51x77wrKU9xT0S1U7adyO0in5Y1B9%2F5fGUqKwiHNJRbjHfQV5mcmj6sRJ5R3qY3B%2FDIFS3yJMxyBzDQoPjTBjqkAdG5Fa2zyAvSafV37PG4%2F0LDsIJXCgXr6CtnMauhNDwhzNT%2B%2FT78DpRJmkaiDk%2FnMeB%2FYEPY0UTwcqfFnwdMBFIB7oM%2ByIMzdClLOQxXQcNCh690CoovhMrhuH1jTuBbXmsCMbo4jNndEy5wLlzc8%2F7E0L%2BBszZMNAClx3GwgzKzjYrmMvw6jQvAogX56x6TQ9tL0SzgvyWosEh%2F%2BctuIYY0%2FwYT&X-Amz-Signature=c8df7f3a2efde0828ef9d6fa0a4abf84c75ec99c0624ff799e219130e8e875e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635ELQFKL%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T185458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCIwp7cs1GkMh%2FYb8rRxAUjd15eWPHSiO28mTN%2FVXLyNwIhAN%2Fu%2B4BOP3hMz32TF3SAqbi%2F3g37ExJ70XFsQlCe0XTGKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2FkECNKFTgVUFBZhoq3ANk6z9P%2B3AP%2F%2FP07iJHhl2hRhLAleBcsbGOz8M9ld3yeTpmA5sMXKjTGEf%2FIZLmXWucuIYl7I%2FcuQn%2FraJRtLpZ2yomRpfrNgHiLGoiXXMJlugiTWVeWumpCmAogQfpiLCgymRyhYhMboq%2BWkYenxuulQJesdmFhGwlYbgziRRuAQiWZkwcQrXkSwSMplGxMFIYXoL78ZTncEmT5F2N3ne67zD2Ti1VOft9VVioMZnVbZ2x2yJQSesmxP84O5peF3ims53EJ2wnVzsx2vAubqXhy38%2B0wCUiGsbCEQaxMQmVVpSx4MjjiZjzmDoLXI%2FlZ%2BGBq7w4R%2B8%2B9UwlikVaesO1M0Tkj%2FEiEw%2FAh0PmxgP3DOfd3pJN15pIdBit2H37IGjOOiB2R9A%2FHWb2ywvb09N%2FAwFqK1UkMxz%2FlFSwthgg3e6uj7PJ4JK8%2FyoNUEWpPBw7M5xKNG3oYPUa3W80%2BpqWcBdLYhZ6jVfRVh%2FE2DEtYKvsVLQC%2FYtZ2Ig8gZeq5Tbt0si4176nwi6A3ZgLS8j46XRcrR7R2aoBFbtN6doJziIm51x77wrKU9xT0S1U7adyO0in5Y1B9%2F5fGUqKwiHNJRbjHfQV5mcmj6sRJ5R3qY3B%2FDIFS3yJMxyBzDQoPjTBjqkAdG5Fa2zyAvSafV37PG4%2F0LDsIJXCgXr6CtnMauhNDwhzNT%2B%2FT78DpRJmkaiDk%2FnMeB%2FYEPY0UTwcqfFnwdMBFIB7oM%2ByIMzdClLOQxXQcNCh690CoovhMrhuH1jTuBbXmsCMbo4jNndEy5wLlzc8%2F7E0L%2BBszZMNAClx3GwgzKzjYrmMvw6jQvAogX56x6TQ9tL0SzgvyWosEh%2F%2BctuIYY0%2FwYT&X-Amz-Signature=323ef7009b2f06e5feccc5c475eb2f6eb6a8612edc82f7f553d9760a792c867f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







