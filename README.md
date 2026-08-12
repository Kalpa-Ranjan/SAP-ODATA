



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R776WFQN%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T071553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkjWH5UGt5yt5eFbF%2Buy5dmFbdjIsAmta%2B3BELpNVUKAiEA3XkWDTDhBrgwe%2B%2Fm5Qfh6xBYPPybh8PAZ52vUbqSBicqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXhE2qoD9I20H3SCrcA2CWuwu9eAf8VdYcV9AyxoSdlEz8vAslwPqyIGdoDtkzzm2baF%2FqN75zujgCBN6sPdB0DniOR1AIg67%2BCsIsqJAYuBLkDVr52n00bPHXo5wPDPdYz0CniHoNN%2FxWSWZY4PK2dUD7W0le8AOHik4UOgCLgsqweP5yxH7rZ4nMvI%2FakT20Kc3th5uP96Fp83j0r5kje%2BC2TiqjvS4kBZBMhFQY8ijGwGHLFET4%2F7e7dSSkpocTYTUZvoPGtO8i8Z1HPLSvjhT7Hs%2BlKoDKqTganShi1DXgW%2BpRNp1ALhow3RukWSnQyLW7z5ao5kmHbJfgCkJtgXHWSZgSxO7Cn6NyFduQ6mN9wcDlvg2y6yFsq%2FblTe8z7qS8arDo%2B%2FgT0%2BSCS1lOauKGRPptW0gCJGn4Up%2BCwuzexrD5y547ETMHPw%2BjMlAnFwwpMzO6%2FNS8OYaWCVdmoC4jE9apSiztY2bQGKmhT6ikAJps9uONamw7Jw8QyzqQDzqorWhGHg10RD6K2WXehEaa4D1Cn157qrNGhh%2B9QqsL1rmBUkmMov2%2BmuBji8Q0cWug11IpMxoL7vkm1%2BnNocpcf0tmzU5pmgu1Kznqh2aQYmsBF%2F7F1Fj9%2BbPl8NmPC6CSLT9vSxURMOGT8NMGOqUBhyBvXb%2B3WBGenVa5TyfStiSRK4JHEoyzU95QIdxLzcTdIFwSB1NGC0f3A7osrexVN%2Fq3N7iHz2eiV7PySnhoPlM4D%2B7t8tcyVJ5otaB9qeJO1q1QUKyuZuJX6%2Bl9Bfn1IIC3acKEVRVLFw%2BkKsloOE3MGXHtaxiQ3IGNxHtG9b0liXZbSmK4HmIqazzWQbLkl0SPG4NNeBCucu%2Bc0vAP40NUWtk6&X-Amz-Signature=f762623722cbbf5a55889aa80c0ad3faf906f139fb1fdf5ef1829f5cce9e3c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R776WFQN%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T071555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkjWH5UGt5yt5eFbF%2Buy5dmFbdjIsAmta%2B3BELpNVUKAiEA3XkWDTDhBrgwe%2B%2Fm5Qfh6xBYPPybh8PAZ52vUbqSBicqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdXhE2qoD9I20H3SCrcA2CWuwu9eAf8VdYcV9AyxoSdlEz8vAslwPqyIGdoDtkzzm2baF%2FqN75zujgCBN6sPdB0DniOR1AIg67%2BCsIsqJAYuBLkDVr52n00bPHXo5wPDPdYz0CniHoNN%2FxWSWZY4PK2dUD7W0le8AOHik4UOgCLgsqweP5yxH7rZ4nMvI%2FakT20Kc3th5uP96Fp83j0r5kje%2BC2TiqjvS4kBZBMhFQY8ijGwGHLFET4%2F7e7dSSkpocTYTUZvoPGtO8i8Z1HPLSvjhT7Hs%2BlKoDKqTganShi1DXgW%2BpRNp1ALhow3RukWSnQyLW7z5ao5kmHbJfgCkJtgXHWSZgSxO7Cn6NyFduQ6mN9wcDlvg2y6yFsq%2FblTe8z7qS8arDo%2B%2FgT0%2BSCS1lOauKGRPptW0gCJGn4Up%2BCwuzexrD5y547ETMHPw%2BjMlAnFwwpMzO6%2FNS8OYaWCVdmoC4jE9apSiztY2bQGKmhT6ikAJps9uONamw7Jw8QyzqQDzqorWhGHg10RD6K2WXehEaa4D1Cn157qrNGhh%2B9QqsL1rmBUkmMov2%2BmuBji8Q0cWug11IpMxoL7vkm1%2BnNocpcf0tmzU5pmgu1Kznqh2aQYmsBF%2F7F1Fj9%2BbPl8NmPC6CSLT9vSxURMOGT8NMGOqUBhyBvXb%2B3WBGenVa5TyfStiSRK4JHEoyzU95QIdxLzcTdIFwSB1NGC0f3A7osrexVN%2Fq3N7iHz2eiV7PySnhoPlM4D%2B7t8tcyVJ5otaB9qeJO1q1QUKyuZuJX6%2Bl9Bfn1IIC3acKEVRVLFw%2BkKsloOE3MGXHtaxiQ3IGNxHtG9b0liXZbSmK4HmIqazzWQbLkl0SPG4NNeBCucu%2Bc0vAP40NUWtk6&X-Amz-Signature=94417872664336f739c02a0ef26c4f4b53b9b56784e23b9ad2d3a1191db324fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







