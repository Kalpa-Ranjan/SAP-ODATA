



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S33V7AF%2F20261026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261026T133407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDEwFq6Xaer%2FzNOueOHtIe9o2IJfq5esddBuMSC%2FNM99QIhAPH1umKLbj46z2zyr4MepsdO6Gl1vsHrx8wEh2Vl4upMKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyps6Iu%2Fr5H56Miumcq3AOdMp%2BHDsJQaniL3lcv36DHae1sMrskEpakOt5Yv8dZoulhn%2FLPIFKs7toYyBWpYp9EOfwkHfdiVr5fRfjVb9uvgCMFumUrymYf6Jb4I1lJNXEv7U7NliKneGTnPdW9EmWwKHkurWeK5Wpg428QvFWTYFH%2FwZXwKrvRr%2Fl8WZKhWJk11n%2BlCGbg7hLl9NIC3CdcqxOY7IgPUCzYCUauzcov0XxBOlDT5CB9%2F4dPACMGKAc%2B41CQzSPDJKCwD2dF%2BKdv1t1tRY9sDYVI8uk09iQ1TzMuG9V%2Bgx%2FyA9hdXop0N%2F5Q0rGl7yGMVDKnFt2rOud7zXvCZzUurhysleGMpZE4PqUgnkD02qu%2BIdb4WhN8Cm03S9n6fCW938TNF00QUnfXRs8LclP84cCUH3UF0OQUpl%2B%2FlZcZgMLS5dOtF7tdcy5NyHFLD2A1gOOvNoBKAiv6VkvbjMxOxzPKFcufr1gEnGSvnvRAZDjTVufyprdjwpKJ0V1TRMPzNo9xUC9b968Bb4fubfm7KALys62F4ezWXXTCXYvRhy6ukVtZnH4jHe4ZufimAJBMhTjD%2BMAyG8qoasLIaN7MHJSpDn5AwkYMnieQhZCsfTHUsmgaauaAgwRSedXYRir3qi%2B96TCBn%2F3WBjqkAUOI96YJCHP270QvA7uJvJ%2FytR1RWc2the%2BstFbh0X%2F7Y60xTy1hIIwguzpRGDtCIUlrYJoZeoTsRAp%2BG8TXLqJkqGntlu39klya3gX5vE5uWMBxIEpke2HtgJKE96Zff7Rf2DucxumJ6HldVFUek85q1fIEhLLeicJyTHihA1%2FdcZYePLw0tOUUlGcMQB6z1atPHIBx1Wn8mCRZnrsrVfOXO01O&X-Amz-Signature=0fb9b677841642fce07a469722c610eef46a262f37b4cf9cb3fadd2b47caf46e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S33V7AF%2F20261026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261026T133407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDEwFq6Xaer%2FzNOueOHtIe9o2IJfq5esddBuMSC%2FNM99QIhAPH1umKLbj46z2zyr4MepsdO6Gl1vsHrx8wEh2Vl4upMKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyps6Iu%2Fr5H56Miumcq3AOdMp%2BHDsJQaniL3lcv36DHae1sMrskEpakOt5Yv8dZoulhn%2FLPIFKs7toYyBWpYp9EOfwkHfdiVr5fRfjVb9uvgCMFumUrymYf6Jb4I1lJNXEv7U7NliKneGTnPdW9EmWwKHkurWeK5Wpg428QvFWTYFH%2FwZXwKrvRr%2Fl8WZKhWJk11n%2BlCGbg7hLl9NIC3CdcqxOY7IgPUCzYCUauzcov0XxBOlDT5CB9%2F4dPACMGKAc%2B41CQzSPDJKCwD2dF%2BKdv1t1tRY9sDYVI8uk09iQ1TzMuG9V%2Bgx%2FyA9hdXop0N%2F5Q0rGl7yGMVDKnFt2rOud7zXvCZzUurhysleGMpZE4PqUgnkD02qu%2BIdb4WhN8Cm03S9n6fCW938TNF00QUnfXRs8LclP84cCUH3UF0OQUpl%2B%2FlZcZgMLS5dOtF7tdcy5NyHFLD2A1gOOvNoBKAiv6VkvbjMxOxzPKFcufr1gEnGSvnvRAZDjTVufyprdjwpKJ0V1TRMPzNo9xUC9b968Bb4fubfm7KALys62F4ezWXXTCXYvRhy6ukVtZnH4jHe4ZufimAJBMhTjD%2BMAyG8qoasLIaN7MHJSpDn5AwkYMnieQhZCsfTHUsmgaauaAgwRSedXYRir3qi%2B96TCBn%2F3WBjqkAUOI96YJCHP270QvA7uJvJ%2FytR1RWc2the%2BstFbh0X%2F7Y60xTy1hIIwguzpRGDtCIUlrYJoZeoTsRAp%2BG8TXLqJkqGntlu39klya3gX5vE5uWMBxIEpke2HtgJKE96Zff7Rf2DucxumJ6HldVFUek85q1fIEhLLeicJyTHihA1%2FdcZYePLw0tOUUlGcMQB6z1atPHIBx1Wn8mCRZnrsrVfOXO01O&X-Amz-Signature=c1f16b59f71c53dd3b6e11c2725a464c49153a912e76e57ddeb7dfed0882af63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







