



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466447IAWEC%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T084827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBU3AnMuE8cJBbyWz5znnc9RTA46vvwAtglQgKyL30uAAiB8ubKcdE8gorYM0u27o5Erj23IGQT2r02qKW%2FOzIlXHiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyGTjGWL5hJNaoX79KtwDII1DdcSGMjIxIdFeucSoas9p69koRSFLyHcfB0ucVBTMMGMDGywAAWSNf%2FctBesZ7%2F9apHVpCVs5WiiBNmVn9aWVPQqOM8k42hj%2FV%2FAQcQO2Tiyzv3H80qj16nkKPXvBeicm6nWF1597GXshnFSbQ1bL51UwGp04QUgzDuq1jvA2ZvcqrUsTK3Dliy8TpsRgodeAH5Dc28PrKbjI2wzGeqO2pQX7TvFAgWs%2FE2xq7d8E4sF1TUfhBwU67CQDym44JHahhJvu1xq91n1s7efRrHe9aXf3L4A6W75UlNLUz4UPWIeVrL%2FT%2FKt7gYW9StXY8tM%2Fj7mDcL0llh9bQHqsEriYpZrBkORpts0pcvtb32CwOlaMBCXRR435Roav1HHdJ3NUZpu1pRGVyoAaQKbu%2F2MnvKq4VIrJxCxevcP7VVh5PWMn8jYv4BqGkXW76o%2BuEjZdt2H0U3dtPSGwveCLjZl8kO5P4aS8DV7ZxvmyKau1DOUos8%2Bjs6pPn7AUXxjFyrcOYHiy67776LYHFA%2Fre1Ij9YcFLoOV37DgOCoa89GOmaP56Y3tBtL%2BxPdcmTHXRXQ%2F0LHlWzyiOrLzCl3hh4N1yC7QeR1lCEQWkx5sEXC2Wjy64jaSvgPiOLQwyZ330gY6pgHCPOVnLurAGHpSG3s%2FVqVBGx3tJr3YJjJ6aJJblweRCBlZxwycfSnwp9qGULJaws5HC06CmkROB2Tp7gv2cU%2BO5eeKvqLaVdgmXi2nQwJQx7m46ZwD9eLe00Ora7JmmAUxfFG68N3%2FcLk5XGgsuABoX%2BUi0%2B7IeEbOfVcSFXyk5VhU7ijlNdHnPif4Dv87IAQn5JWVUoz8Yk1gjNoZi%2FJBfzBFtSe3&X-Amz-Signature=3b143fe4e1a96cbc07fccfb2bc2cbc510461523b57719913ebe4778ff1691e4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466447IAWEC%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T084827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBU3AnMuE8cJBbyWz5znnc9RTA46vvwAtglQgKyL30uAAiB8ubKcdE8gorYM0u27o5Erj23IGQT2r02qKW%2FOzIlXHiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyGTjGWL5hJNaoX79KtwDII1DdcSGMjIxIdFeucSoas9p69koRSFLyHcfB0ucVBTMMGMDGywAAWSNf%2FctBesZ7%2F9apHVpCVs5WiiBNmVn9aWVPQqOM8k42hj%2FV%2FAQcQO2Tiyzv3H80qj16nkKPXvBeicm6nWF1597GXshnFSbQ1bL51UwGp04QUgzDuq1jvA2ZvcqrUsTK3Dliy8TpsRgodeAH5Dc28PrKbjI2wzGeqO2pQX7TvFAgWs%2FE2xq7d8E4sF1TUfhBwU67CQDym44JHahhJvu1xq91n1s7efRrHe9aXf3L4A6W75UlNLUz4UPWIeVrL%2FT%2FKt7gYW9StXY8tM%2Fj7mDcL0llh9bQHqsEriYpZrBkORpts0pcvtb32CwOlaMBCXRR435Roav1HHdJ3NUZpu1pRGVyoAaQKbu%2F2MnvKq4VIrJxCxevcP7VVh5PWMn8jYv4BqGkXW76o%2BuEjZdt2H0U3dtPSGwveCLjZl8kO5P4aS8DV7ZxvmyKau1DOUos8%2Bjs6pPn7AUXxjFyrcOYHiy67776LYHFA%2Fre1Ij9YcFLoOV37DgOCoa89GOmaP56Y3tBtL%2BxPdcmTHXRXQ%2F0LHlWzyiOrLzCl3hh4N1yC7QeR1lCEQWkx5sEXC2Wjy64jaSvgPiOLQwyZ330gY6pgHCPOVnLurAGHpSG3s%2FVqVBGx3tJr3YJjJ6aJJblweRCBlZxwycfSnwp9qGULJaws5HC06CmkROB2Tp7gv2cU%2BO5eeKvqLaVdgmXi2nQwJQx7m46ZwD9eLe00Ora7JmmAUxfFG68N3%2FcLk5XGgsuABoX%2BUi0%2B7IeEbOfVcSFXyk5VhU7ijlNdHnPif4Dv87IAQn5JWVUoz8Yk1gjNoZi%2FJBfzBFtSe3&X-Amz-Signature=0b37e148ee55a059d1c14af404c43896a85dea8ae710a54f17a1bfd991bafdac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







