



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWM66EA%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T012752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIHwTh2z629kfPdRqQ2MTFSweyBsC2v60adaI6%2FgN7IiyAiEAtMA5BmsGXwlJgTVcHNebG5ioZIhb0DKoTRTeVuFcj0cqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAw8kSRoWrTQhUh6ircA4d7ADHde4ZIy00ICenIPyxjYRLtmdNynnvz6%2B7o6N%2FwXxCMColywLGJralXRIciT1ng9RR72OyZI5GPkNJUi2RhDOIAOy%2B3Bolo6od1%2FfYFF1ggqmHL58292C%2BrZf2HMsv5KpZM2uP3C4V01iGL74lj17vOINHb2a%2Bcxncps9ai0FscO5QJlAVRCUz%2Fh4zzpfcAbVoPUJUgCRKPRJs2rYY4uNzcqXyv4TIvEZQkiSR%2BY74%2Bv5h7L4CY6muxMpfXqTdrv0zaqPFFlzVtPPrFboCzO%2FTXAH7Idt3ExgFtSDZv1GkMCBAfxwX5huzJHBQRPQ%2FV6MX3VUmS%2BIHRhe7Q2FINi%2B8mVXd6D5dEssLk%2BJ5OwCGkJ3qTalIUaZUJ83aWfYAvnYTJ0m74kuBXSlhnsgPordKGhglsQT8pIUMCtaM2YWOT6xd4PIGwf0dNewYMaUUm5tw7u%2BytEtM0T%2FlLQwoSDZehlT2Kyxo%2FYGsClGB5hqenDiMN4NXGYuLpCoyLjhDvZtmDK4UTtoN6i1M1gQF4uQPe1g9iG6g%2Be9n2vcxTQr33SrTK%2BcInmzo59y7C9gH1CfmHvG5gaiHkxbYLiok9Nr5osUxbOdqJz3yK1Mmz2A3DymQobrSlhy1gMMXorc0GOqUB3aJeYlRVSE3uiQ4oImSZ6geHf7jwIpfenCprJQOCyBs06VahC2bC7hbX%2FaZYdNNRgL7z4cA%2BvB8GZe%2Fmo%2F%2B8%2ByXf9Jyvw66GPuJSXrmKelUJy%2BQV0%2FuOyYKvff%2BwVX2wMRngusO1rlxrSeUazoOGlPfsHAt72B2hg4AbtBVCcDgnp184XXrI8MwK2%2FKSOzMx75XwCTeQ5Klfx7%2BG5WC3PjBlv1Rf&X-Amz-Signature=ced77ceb27ad807b81cc29f960c470a5e95315eb8f640299c23113e457ff51a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNWM66EA%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T012752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIHwTh2z629kfPdRqQ2MTFSweyBsC2v60adaI6%2FgN7IiyAiEAtMA5BmsGXwlJgTVcHNebG5ioZIhb0DKoTRTeVuFcj0cqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAw8kSRoWrTQhUh6ircA4d7ADHde4ZIy00ICenIPyxjYRLtmdNynnvz6%2B7o6N%2FwXxCMColywLGJralXRIciT1ng9RR72OyZI5GPkNJUi2RhDOIAOy%2B3Bolo6od1%2FfYFF1ggqmHL58292C%2BrZf2HMsv5KpZM2uP3C4V01iGL74lj17vOINHb2a%2Bcxncps9ai0FscO5QJlAVRCUz%2Fh4zzpfcAbVoPUJUgCRKPRJs2rYY4uNzcqXyv4TIvEZQkiSR%2BY74%2Bv5h7L4CY6muxMpfXqTdrv0zaqPFFlzVtPPrFboCzO%2FTXAH7Idt3ExgFtSDZv1GkMCBAfxwX5huzJHBQRPQ%2FV6MX3VUmS%2BIHRhe7Q2FINi%2B8mVXd6D5dEssLk%2BJ5OwCGkJ3qTalIUaZUJ83aWfYAvnYTJ0m74kuBXSlhnsgPordKGhglsQT8pIUMCtaM2YWOT6xd4PIGwf0dNewYMaUUm5tw7u%2BytEtM0T%2FlLQwoSDZehlT2Kyxo%2FYGsClGB5hqenDiMN4NXGYuLpCoyLjhDvZtmDK4UTtoN6i1M1gQF4uQPe1g9iG6g%2Be9n2vcxTQr33SrTK%2BcInmzo59y7C9gH1CfmHvG5gaiHkxbYLiok9Nr5osUxbOdqJz3yK1Mmz2A3DymQobrSlhy1gMMXorc0GOqUB3aJeYlRVSE3uiQ4oImSZ6geHf7jwIpfenCprJQOCyBs06VahC2bC7hbX%2FaZYdNNRgL7z4cA%2BvB8GZe%2Fmo%2F%2B8%2ByXf9Jyvw66GPuJSXrmKelUJy%2BQV0%2FuOyYKvff%2BwVX2wMRngusO1rlxrSeUazoOGlPfsHAt72B2hg4AbtBVCcDgnp184XXrI8MwK2%2FKSOzMx75XwCTeQ5Klfx7%2BG5WC3PjBlv1Rf&X-Amz-Signature=e3e1d2a25782ea1264ef783341b3b5575489a08e09cae822d404fb8bb94d19a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







