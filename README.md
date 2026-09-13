



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466527CNVWB%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T002312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4hW26h%2Fmi05Eakbpvvw7b5U1ehnbShp8lgXUXd1faEQIhAO4pf%2BQZdBtjpkl0IEVIRRCI2lLVjTwuGWHktKn1cXpSKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw6r8tYaevURreJZG4q3ANZ1r5ojYrPXo8Zmm8myrV9zYwWbcapdZv8UkpLpyaIVdENky1BiScsPY%2FzK21lTYVSExTMpLT5FxJ1fjFzWoJpDJnGVE5AcZfF29nRFaRHTnG22pzqdV8TJGQnTh9TOf8fShH9pp0agsl8SRWd0sSTtxfR8HNYoarxTSCEnHhGWvlRfddWwikYRpz%2BLo0FsQ%2F2EdlZJLsSUDu1sCJCCFHihsD7d9fPV5nGd2Nza0DgYfEXu63hOaqSGzEENtAPR7lGFHFIW13eyjB1M3Dg2sScfN1cTnoO1beNtnxJbSYnN0id5RvnPf0mPQMmDw%2FWka6GNxEq7t6EWEBjfhlpWsvvpg3vhMNIe0K21nRT%2F%2FYAqbQSjFyrnxuAZIrw1UflFTnNpDGA%2BCHT7n2tPdFzd9M5f8e8Dasgqnu6tuNC%2BGxb4fmD9orW%2BM%2BaYHCjbqthpFl3CsteqENd4hRPBscjG9MZ%2B%2FCnFmlOEMjOpFhfP3MAYwmCNEefqh%2BkFH%2F5BpCnkYhQa9Xh0wtUXnz1GJmJKfH%2BVKIFqNG%2B2qnmyfcgbMcohqDyqZv9ggYM%2BdjANaff98FxqWV5uGZMy71NW2DmwBJXI8ncZx7g5V0vaR3WoFrsde79ZtqQ04ySIqxPnjDvr5fVBjqkAYb%2BjjDY%2FD5HkEVNYJ%2FLyMisa92LZI6z5dqjyNbWQo%2FggoreITxXfsgRc%2FumUUWtoGSL4Kv4AboPQvFITb7UeGUBnDPqdTFOYw%2FbrpR1sip%2Fn5Cd4apB6YrOF4VcG6VI7%2BHR1voSXPupbq%2B%2FqPLD6vXQIYX0tQHIlgHPjV%2BJJoNsgdFNdVglv1l7BWHo04BdTIAJX6zwg9xWWpcuO39qnX7S14EO&X-Amz-Signature=12d7ccaca777e4a3bf538e67a9a4e6233b9309a631862e993c8e557e07580f64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466527CNVWB%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T002312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4hW26h%2Fmi05Eakbpvvw7b5U1ehnbShp8lgXUXd1faEQIhAO4pf%2BQZdBtjpkl0IEVIRRCI2lLVjTwuGWHktKn1cXpSKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw6r8tYaevURreJZG4q3ANZ1r5ojYrPXo8Zmm8myrV9zYwWbcapdZv8UkpLpyaIVdENky1BiScsPY%2FzK21lTYVSExTMpLT5FxJ1fjFzWoJpDJnGVE5AcZfF29nRFaRHTnG22pzqdV8TJGQnTh9TOf8fShH9pp0agsl8SRWd0sSTtxfR8HNYoarxTSCEnHhGWvlRfddWwikYRpz%2BLo0FsQ%2F2EdlZJLsSUDu1sCJCCFHihsD7d9fPV5nGd2Nza0DgYfEXu63hOaqSGzEENtAPR7lGFHFIW13eyjB1M3Dg2sScfN1cTnoO1beNtnxJbSYnN0id5RvnPf0mPQMmDw%2FWka6GNxEq7t6EWEBjfhlpWsvvpg3vhMNIe0K21nRT%2F%2FYAqbQSjFyrnxuAZIrw1UflFTnNpDGA%2BCHT7n2tPdFzd9M5f8e8Dasgqnu6tuNC%2BGxb4fmD9orW%2BM%2BaYHCjbqthpFl3CsteqENd4hRPBscjG9MZ%2B%2FCnFmlOEMjOpFhfP3MAYwmCNEefqh%2BkFH%2F5BpCnkYhQa9Xh0wtUXnz1GJmJKfH%2BVKIFqNG%2B2qnmyfcgbMcohqDyqZv9ggYM%2BdjANaff98FxqWV5uGZMy71NW2DmwBJXI8ncZx7g5V0vaR3WoFrsde79ZtqQ04ySIqxPnjDvr5fVBjqkAYb%2BjjDY%2FD5HkEVNYJ%2FLyMisa92LZI6z5dqjyNbWQo%2FggoreITxXfsgRc%2FumUUWtoGSL4Kv4AboPQvFITb7UeGUBnDPqdTFOYw%2FbrpR1sip%2Fn5Cd4apB6YrOF4VcG6VI7%2BHR1voSXPupbq%2B%2FqPLD6vXQIYX0tQHIlgHPjV%2BJJoNsgdFNdVglv1l7BWHo04BdTIAJX6zwg9xWWpcuO39qnX7S14EO&X-Amz-Signature=972b75decdf8fe5300e090dad07f2e61fdd5e98f8aa73a6a8fc9fd0d99ba5bef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







