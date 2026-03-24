



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTRJIFNJ%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T014356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAu6%2Bx%2BbjWllt2Kdfyau7wkv8HSkyVO78B719oD%2BXL6JAiAxtbPokM5H7OXnb7Zz6J1FwmMGa55ChxBpJ%2BFGkGWwxiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBCiiw%2F1joSiAMtNKKtwDY9zRZDP%2Fn0R3CkBW0MkKliwEJxN65FYLbl%2Bu%2F0bhvHaW3BlsPtSzBZW36ceSDyf0L69ztigk98NHwdWKV9aWepz1PYC8xYL4gSc%2Btx59u%2BZjEjKg%2FmLL0cn9mpGZVf1%2Fr18DMZZS%2F2hwz7KN21eJgJd6uqh7GLhv9uk%2F13vPRPgDlqZ3t9he4vmSXYeG%2FkhIc%2Fu1tHhCk0lWjppjLyDq6emzvv5rQ6r%2F9XClBpYjiDSSiAU1dUWJH1RwrdZX2SI0u%2BC1UwZLlbxWy4sVnsfenu1iHtYIrnLw7jZAp%2FKj2pRBA2TmlImuakRMtgnMubmFmE%2FCQEOwKUmY3slTfBz%2F0BeHWVVbNpmoRDsRRVh%2FaDT8XLk69sEpWDHoSvjk8oK%2BdCBzR%2FtzYlSLUNERiWeh1%2BPn7x%2F6utNkjy%2BnVRteO6wWTKEMyrhf7GTK7deci9kJZroFQJOVFT5DAHcfxaf6aD0%2B4T4o74I6aWBBq%2BBZDoq6zRO5fqglcq2EMe%2BmrHcdvYymIU2ktUVhn6TCr%2F33mDS5slvRH76SeuKK9sbe9Uo%2B%2FEymhoPJ27kb9b%2FyPiNQHJGKmTtjVSuc2XFaKt321yXSY3L%2BEtKnTkP4iAMzSpfrsdn0kYGnp5%2FjqOowosmHzgY6pgF9me6OWLofRr6oU6lwqU55tSYtcf3nCQIkSiIzl%2FuQGOuyRxMy4THhQafqowH4LiLBmlM8OvOKvitbg6WwPrvr9%2FL9XjxIKUGDWJAW11qBEsPoY%2FYwqPdkD3tXDjfUSQ6oDFYUXnZLhjgW6fMlA8OAeDCObC9Xi4JZdMlNSVSkHWxEHg4Ur9C80gzYjLFjN4nA%2BRdxCzMBgMZJdy1meJ7%2BbJWLVTWO&X-Amz-Signature=e81ed4f369010ac8740ca2f47c021f04c82bfaebb95fdc4bbd340f8cdc6a3fe9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTRJIFNJ%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T014357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAu6%2Bx%2BbjWllt2Kdfyau7wkv8HSkyVO78B719oD%2BXL6JAiAxtbPokM5H7OXnb7Zz6J1FwmMGa55ChxBpJ%2BFGkGWwxiqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBCiiw%2F1joSiAMtNKKtwDY9zRZDP%2Fn0R3CkBW0MkKliwEJxN65FYLbl%2Bu%2F0bhvHaW3BlsPtSzBZW36ceSDyf0L69ztigk98NHwdWKV9aWepz1PYC8xYL4gSc%2Btx59u%2BZjEjKg%2FmLL0cn9mpGZVf1%2Fr18DMZZS%2F2hwz7KN21eJgJd6uqh7GLhv9uk%2F13vPRPgDlqZ3t9he4vmSXYeG%2FkhIc%2Fu1tHhCk0lWjppjLyDq6emzvv5rQ6r%2F9XClBpYjiDSSiAU1dUWJH1RwrdZX2SI0u%2BC1UwZLlbxWy4sVnsfenu1iHtYIrnLw7jZAp%2FKj2pRBA2TmlImuakRMtgnMubmFmE%2FCQEOwKUmY3slTfBz%2F0BeHWVVbNpmoRDsRRVh%2FaDT8XLk69sEpWDHoSvjk8oK%2BdCBzR%2FtzYlSLUNERiWeh1%2BPn7x%2F6utNkjy%2BnVRteO6wWTKEMyrhf7GTK7deci9kJZroFQJOVFT5DAHcfxaf6aD0%2B4T4o74I6aWBBq%2BBZDoq6zRO5fqglcq2EMe%2BmrHcdvYymIU2ktUVhn6TCr%2F33mDS5slvRH76SeuKK9sbe9Uo%2B%2FEymhoPJ27kb9b%2FyPiNQHJGKmTtjVSuc2XFaKt321yXSY3L%2BEtKnTkP4iAMzSpfrsdn0kYGnp5%2FjqOowosmHzgY6pgF9me6OWLofRr6oU6lwqU55tSYtcf3nCQIkSiIzl%2FuQGOuyRxMy4THhQafqowH4LiLBmlM8OvOKvitbg6WwPrvr9%2FL9XjxIKUGDWJAW11qBEsPoY%2FYwqPdkD3tXDjfUSQ6oDFYUXnZLhjgW6fMlA8OAeDCObC9Xi4JZdMlNSVSkHWxEHg4Ur9C80gzYjLFjN4nA%2BRdxCzMBgMZJdy1meJ7%2BbJWLVTWO&X-Amz-Signature=85dd28b4a0cd73d894fef32c473099be335fecc5c1b8bfec73803e3ec027a29f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







