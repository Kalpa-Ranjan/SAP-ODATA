



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BQPATAM%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T063030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIEgsIVdSKby7fMdyETb6EVVQwtrP2cwbIympkFBZh3pnAiEAxL6HNXGPfhySn4S2F755LfotH4o6eI%2FgzIFytl6%2FWTcq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDAgTNcBxNbKdWdct%2BircA8%2BmHO2ne%2Bl1A2fUmr4y1rvrIJ9z9QdbE2bE0zGDVpLHfiIrKTf%2Fs%2BqOJa1ou6ixxGobSza%2FNzF8UjP9B5NSnxFn%2Ft09nkQTy55y9MdvSpKJr6FseCGNSDr3HJQwMEIpVWrFOTcpHaKdKUv3Xiy8cvQVPEKEHy2741rgn7JBUyQOA0j72eqxehv4EevSIKR1RgQuLAA0%2FJW%2F7sa%2B%2FVJ6hqTmh47KqvgL%2FVjlFUaa0HoKgrUDscjKa5x%2Bx%2BX%2FthKIkh8j7loZS6xkCarU%2BDNjheKAWc8j0j%2BxNnOtutdZEQPWTwT4OJQeTBLHQe92fxyhU1MVjdCnuzfPxNHhuudeq%2BOXhuQkmPuquYKbKv6vKEGchf2bLBgl0GPNFMQPLSvPkvxakECPD%2BJ8FnYgV7x3vSG3JpcUpX6DejZzl0i%2B0UDn6nUhU6Zhd1nq8o5Dl3z27xNQLCCpTbM4IHtujhao9FlQH7u5gPO7RfY1DhVUHpCQ9OWHwOnzc1rvReXT%2BLwuPurfj7hW%2FkgUgvmkW65Og7QqjjwVE5VlmQdqh3rBmZ8Q52%2B9%2BUxSpuuZfNRluLSF8ielgLI4%2BAAlPEoYqxdJunVkSjpaeRRFcexeFFLk8PCB2PgiOKfkDUsb787LMPCQ3MsGOqUBabARJ%2BolJgUPiJMWfWG3iGU2YN7bEZHap6%2FnNq1AxajtfqWiH%2Bsy3mb4ur0I%2FKWfW16olJpx64ySsPOHLikQqNfKQUGrunTtNZUu7Dv3SuRlgR76oTAiuZUygLCDzHMHAI%2Bd4yza92j3UUuaMICPLzwnl9RBp%2Bkqd9qNEFd0bt4Iy15LOXZHEoWRdztLkXFAe%2B%2FT8uV4V%2F0UwSQyg0f%2FTUrXlW60&X-Amz-Signature=c18d0d0c92353a1aad95045b1e5e4bc715b29b7d7613048a684026e9866f9fca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BQPATAM%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T063030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIEgsIVdSKby7fMdyETb6EVVQwtrP2cwbIympkFBZh3pnAiEAxL6HNXGPfhySn4S2F755LfotH4o6eI%2FgzIFytl6%2FWTcq%2FwMIOBAAGgw2Mzc0MjMxODM4MDUiDAgTNcBxNbKdWdct%2BircA8%2BmHO2ne%2Bl1A2fUmr4y1rvrIJ9z9QdbE2bE0zGDVpLHfiIrKTf%2Fs%2BqOJa1ou6ixxGobSza%2FNzF8UjP9B5NSnxFn%2Ft09nkQTy55y9MdvSpKJr6FseCGNSDr3HJQwMEIpVWrFOTcpHaKdKUv3Xiy8cvQVPEKEHy2741rgn7JBUyQOA0j72eqxehv4EevSIKR1RgQuLAA0%2FJW%2F7sa%2B%2FVJ6hqTmh47KqvgL%2FVjlFUaa0HoKgrUDscjKa5x%2Bx%2BX%2FthKIkh8j7loZS6xkCarU%2BDNjheKAWc8j0j%2BxNnOtutdZEQPWTwT4OJQeTBLHQe92fxyhU1MVjdCnuzfPxNHhuudeq%2BOXhuQkmPuquYKbKv6vKEGchf2bLBgl0GPNFMQPLSvPkvxakECPD%2BJ8FnYgV7x3vSG3JpcUpX6DejZzl0i%2B0UDn6nUhU6Zhd1nq8o5Dl3z27xNQLCCpTbM4IHtujhao9FlQH7u5gPO7RfY1DhVUHpCQ9OWHwOnzc1rvReXT%2BLwuPurfj7hW%2FkgUgvmkW65Og7QqjjwVE5VlmQdqh3rBmZ8Q52%2B9%2BUxSpuuZfNRluLSF8ielgLI4%2BAAlPEoYqxdJunVkSjpaeRRFcexeFFLk8PCB2PgiOKfkDUsb787LMPCQ3MsGOqUBabARJ%2BolJgUPiJMWfWG3iGU2YN7bEZHap6%2FnNq1AxajtfqWiH%2Bsy3mb4ur0I%2FKWfW16olJpx64ySsPOHLikQqNfKQUGrunTtNZUu7Dv3SuRlgR76oTAiuZUygLCDzHMHAI%2Bd4yza92j3UUuaMICPLzwnl9RBp%2Bkqd9qNEFd0bt4Iy15LOXZHEoWRdztLkXFAe%2B%2FT8uV4V%2F0UwSQyg0f%2FTUrXlW60&X-Amz-Signature=e0fbeb02f78d8379c1d1dc4139788b14dece783a5fcdb780fd40616404e52495&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







