



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUFAE2N%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T062434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEJkD%2FbumY3Rh8QQqvJ11AQVX7o7KYs%2BmG5glBOs5gKAiEA57GZ2TXqDTLUciY5rLrBew7iY2Z6f%2FXKgZjTyv%2BU20UqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqu75us4uKd89zbPircA6a%2BBYoZElANrUIGQ6jGwxXI714uXnyVtbz5c4subsyCjqKaF7J8E8vQTiDugMsf5TocX6bV%2BTwT9EnMjlnmjAJ0pMJUgUYnnpYaWengYM%2F5anuUtYSqQRpv%2FB4uNsrDxmSzMJ%2FQ7J9RXZIHp26fso27pAQMElChxutrGuNkEqdNzk%2FT%2BD8wKHpbAAoa%2BCH%2B%2BvmiKZpkrFXleuucyEHRrj4QhU7%2BoKKb%2FXwo6Sol43k7ZXHNyMUT1dY76gz%2B53Z1aAcL6qqyVrp8cyd2WvuTsJsl4BSdBkP7c3Ld22i9aC58r9%2FTt79BbbAtxWMmSbZ0KKOgp5RnXvhYrDLPjtj9LA%2B3dUDeWSF12ojggX8VcA5VAnnImDxIntkhTc%2FX3%2FiX89HQoSllf%2FyTb66FwmEez1ncuCEWtc%2Fgvy37bY0KVFwv9zvSQYzJmVZn660%2FHPNYHuRoEnGbROQ%2BTzEkw3gnP5LtpHfEL8Ij3kB3kyO098Hjfz2gvifc8wJJvTuN8XcFiLpG2OKAyRVZKcNXnd6wWgxByGwc50%2B6gbSZfkiGRRAmrSAheJ1CANZOpN5JOp%2FV5aKTueXUE7jdXNmRvA%2FgI%2BKzrWwdN%2FdZAmPpU6OayYtRM4POYxPJS3AvSpswMIzV6sgGOqUBH%2FdcIdW8%2BokUpsqAgvd92XiqjVn8CxHhr4H5QgnSV0bAAbjHDacflI%2BtM44HUPjU8XGnX5qp3mdLBl8Pfic%2F2KTUotRtQopmi9J%2FRp%2BEh2nLgZnfhqNWrbnAmt7PmnsaJNwtvXVOF8F%2BJokQoSX1kxWLmZpdNiHTSWP2H4IJit7NX7hWV%2B81t6%2FWRtiKrdY9DkajZsdxB%2BD2ndPL6Tz%2BS9be7cIy&X-Amz-Signature=d5461ca9d124e616faa4d53da2094608cd8913eacd0c8c87adb3f9f6d6e26b73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUFAE2N%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T062434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEJkD%2FbumY3Rh8QQqvJ11AQVX7o7KYs%2BmG5glBOs5gKAiEA57GZ2TXqDTLUciY5rLrBew7iY2Z6f%2FXKgZjTyv%2BU20UqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqu75us4uKd89zbPircA6a%2BBYoZElANrUIGQ6jGwxXI714uXnyVtbz5c4subsyCjqKaF7J8E8vQTiDugMsf5TocX6bV%2BTwT9EnMjlnmjAJ0pMJUgUYnnpYaWengYM%2F5anuUtYSqQRpv%2FB4uNsrDxmSzMJ%2FQ7J9RXZIHp26fso27pAQMElChxutrGuNkEqdNzk%2FT%2BD8wKHpbAAoa%2BCH%2B%2BvmiKZpkrFXleuucyEHRrj4QhU7%2BoKKb%2FXwo6Sol43k7ZXHNyMUT1dY76gz%2B53Z1aAcL6qqyVrp8cyd2WvuTsJsl4BSdBkP7c3Ld22i9aC58r9%2FTt79BbbAtxWMmSbZ0KKOgp5RnXvhYrDLPjtj9LA%2B3dUDeWSF12ojggX8VcA5VAnnImDxIntkhTc%2FX3%2FiX89HQoSllf%2FyTb66FwmEez1ncuCEWtc%2Fgvy37bY0KVFwv9zvSQYzJmVZn660%2FHPNYHuRoEnGbROQ%2BTzEkw3gnP5LtpHfEL8Ij3kB3kyO098Hjfz2gvifc8wJJvTuN8XcFiLpG2OKAyRVZKcNXnd6wWgxByGwc50%2B6gbSZfkiGRRAmrSAheJ1CANZOpN5JOp%2FV5aKTueXUE7jdXNmRvA%2FgI%2BKzrWwdN%2FdZAmPpU6OayYtRM4POYxPJS3AvSpswMIzV6sgGOqUBH%2FdcIdW8%2BokUpsqAgvd92XiqjVn8CxHhr4H5QgnSV0bAAbjHDacflI%2BtM44HUPjU8XGnX5qp3mdLBl8Pfic%2F2KTUotRtQopmi9J%2FRp%2BEh2nLgZnfhqNWrbnAmt7PmnsaJNwtvXVOF8F%2BJokQoSX1kxWLmZpdNiHTSWP2H4IJit7NX7hWV%2B81t6%2FWRtiKrdY9DkajZsdxB%2BD2ndPL6Tz%2BS9be7cIy&X-Amz-Signature=3b8cf9ab7ee33596fe52813b7269872c105ab895bb85f44248e71aa3b43a0dd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







