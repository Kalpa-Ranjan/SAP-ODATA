



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C5QOKXG%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T124251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxi5QAaqHeXpAM5%2F7YnCoJ7iyIcIGgs%2F33HPgeqhkOagIhAOXw%2FUURJ%2F7vRvLe29eSwVkwn26tbqz036x3wYD5YM29KogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4KUVg%2BBH1Zas2f%2Foq3AP1ah8UY%2BFtUBV%2Fxlnph8GvFeBUpGqk8q26snGEQJ9v6o9ptDj1G5Ujt1p%2FIYhubNz1tYkvf%2BRSRdZQifG5jBeTywdhLI4SylD0bIFIWatSmoOZErYyu1NlmUTJFzBshulYzjWIekpOKYQgHVF80o2YiIxwu631e7I61yrLfObthf28x71TcXZMBQGWDDXjy7iDwL3yDvZLiRKy%2FCEU%2F6Vquc3KloZaPnKk9wziDHiL1RoXu%2BTEdiKQAmtvr5uAnbASvfr%2F%2FMtReci0BxZVdDMg%2BKFpVLlBdQWRf7J36R8KIga%2BwY4xQIiajPPZxJ5%2BQceLf3%2BCGrjcBDlQkgKEpq%2FFT%2BuMhUEp1E0QlGSXm6xy%2Bx7pO13jSYsWA7eNpCtABfSEsMPWRMFE6arb12P6iE0WzpqZP3JFLIo0miTlAkn4qc5ZGi32H3a9XLWSEVnhr016C3Ddw419azuF%2FLzNM6gBLeFTmZyyCT%2FbtEousa4BxP1T0PZ8c%2Fj3wq2cAyQOpbI%2B2th6FSI0pOdpxH2lvifYtUShzmRp7a9DXfyuc87I2rAJz6IrHPdd5%2F8qlzPY%2Fv9QVQorLKzT2y8gyZ7VSz8xSb0IWH1Uev5GqXe2GoE4v3ZoBg4wg5gR78g1RTDyhJvNBjqkATOV335u3lg9q6Bc83RPDfKheat%2Be01XXRjWfyNYFyw2eEdRDa%2Ff%2FWdz%2FfSmFDa2GtTyRwqAImxvtTLVR3EOlYf4RCwpDhPrsVFioQCa9wFPitJAkecoOSDvoqO46A%2F%2FFp%2B40D2acfCD6byI4cMzYQY9KzYIu84wFjWs8WzR%2B3CjeabQuQRUH3KnyYduT0JwyeQuvNbk3dp0BX2xUIQu0qdLhla9&X-Amz-Signature=ac836cda52ed4fa7eaf99642f9ba9fc7b8188b83abfc92772951a075be00a0d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C5QOKXG%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T124251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxi5QAaqHeXpAM5%2F7YnCoJ7iyIcIGgs%2F33HPgeqhkOagIhAOXw%2FUURJ%2F7vRvLe29eSwVkwn26tbqz036x3wYD5YM29KogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4KUVg%2BBH1Zas2f%2Foq3AP1ah8UY%2BFtUBV%2Fxlnph8GvFeBUpGqk8q26snGEQJ9v6o9ptDj1G5Ujt1p%2FIYhubNz1tYkvf%2BRSRdZQifG5jBeTywdhLI4SylD0bIFIWatSmoOZErYyu1NlmUTJFzBshulYzjWIekpOKYQgHVF80o2YiIxwu631e7I61yrLfObthf28x71TcXZMBQGWDDXjy7iDwL3yDvZLiRKy%2FCEU%2F6Vquc3KloZaPnKk9wziDHiL1RoXu%2BTEdiKQAmtvr5uAnbASvfr%2F%2FMtReci0BxZVdDMg%2BKFpVLlBdQWRf7J36R8KIga%2BwY4xQIiajPPZxJ5%2BQceLf3%2BCGrjcBDlQkgKEpq%2FFT%2BuMhUEp1E0QlGSXm6xy%2Bx7pO13jSYsWA7eNpCtABfSEsMPWRMFE6arb12P6iE0WzpqZP3JFLIo0miTlAkn4qc5ZGi32H3a9XLWSEVnhr016C3Ddw419azuF%2FLzNM6gBLeFTmZyyCT%2FbtEousa4BxP1T0PZ8c%2Fj3wq2cAyQOpbI%2B2th6FSI0pOdpxH2lvifYtUShzmRp7a9DXfyuc87I2rAJz6IrHPdd5%2F8qlzPY%2Fv9QVQorLKzT2y8gyZ7VSz8xSb0IWH1Uev5GqXe2GoE4v3ZoBg4wg5gR78g1RTDyhJvNBjqkATOV335u3lg9q6Bc83RPDfKheat%2Be01XXRjWfyNYFyw2eEdRDa%2Ff%2FWdz%2FfSmFDa2GtTyRwqAImxvtTLVR3EOlYf4RCwpDhPrsVFioQCa9wFPitJAkecoOSDvoqO46A%2F%2FFp%2B40D2acfCD6byI4cMzYQY9KzYIu84wFjWs8WzR%2B3CjeabQuQRUH3KnyYduT0JwyeQuvNbk3dp0BX2xUIQu0qdLhla9&X-Amz-Signature=84afc1eca6e0c00482f5baa08a7006b67b2d1d27b4c6df0529667af24f558ce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







