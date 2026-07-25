



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS3MPBEB%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T075828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFIyXYq4QfdziyLcQTDwGuUX%2BuGTsnXV%2Fgk7%2BfeA0Mw3AiBdFGP%2B8%2F2zB6A6DBHyIDcvVK%2BaCdL%2BPMuCeKWZWSVvJCr%2FAwgYEAAaDDYzNzQyMzE4MzgwNSIMYhP5DwB10bX46MeFKtwDZ7yzU03ATo747fx9Jmby0zfzflfJ48Fu84So7Qj1bxg1L09WX9kJiM048%2BvdBu83KNiRwNqEMAcqqs9UcbRt%2FM8k%2BtFJpBs6v6viF7sVip4wjrg6a255ukCCV20NPe76y0QnGZ3Qt7jm6r3g3kQvfFy3ad5PeNd1UxtiyjZ0lbFBE65tU0V1H2nn8mUISMylSnAtlH6rQ8JApOhLtvwd36LOULnz%2Bgq5p4PmlL4PvasmaN2GOFURfzKmD5UGUss8rfWGLPYUVbOlQF95ZJcHK2DV2SBSHdxZRMYRDmfHFnJOdf85zuByhaAaRzCzbjRQvdpm1C6mhp7mpnjJ4oSqk1%2FL2HzBxtqdlsOMTHVtq9QQB6rIhsBumRiI2uUm3XGhdEgOL%2Bh1QTTEhnfetGJueE7DMRXGfVjIGTYNT2%2F4UIrjkrEcuz44wuMNxIbxwEKU9zpuVSmeP4PI5Soigkmpt6a%2BZbp1XD81eT1%2BmglfVM9GBbSyOkFb3ocZU0kVeETc0jhBMCf51HMEVs6kuuJverRZVdF5nP8%2BWPa11PGlB8jCMTF6yeJVsniR%2F0Sx62QQWg50ZPDT3PSRKRX2eeZDJ0vTq3l5fPAMTDFJwICcAWVOq%2FludvaWSEKFnhowmcSR0wY6pgHhrT%2Bb3CnjFnB%2BFFmjkRRMl6HlTh4Oken0qakkf1fsuHOnMIr1ty6Ro1ekmxATso908dIc7VxAS10PJZ%2BThRebOzJPlbaYLcU00zxk77MR9mzGBragYLRpwVxy4BCco3AnG%2BgE0vEtMIIahuBicYth7OTh9z5gCrTh4VqgTOIuHMH6F%2FlMNdrk1hEO1w3Fp2o3%2Bfr1TWDDVlPSNgCvz24xnk8rpHSz&X-Amz-Signature=28f06ae0c84a7f644eb1d1f012a2ca3339ececf3310676ed4fde0e3e38699e33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XS3MPBEB%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T075829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIFIyXYq4QfdziyLcQTDwGuUX%2BuGTsnXV%2Fgk7%2BfeA0Mw3AiBdFGP%2B8%2F2zB6A6DBHyIDcvVK%2BaCdL%2BPMuCeKWZWSVvJCr%2FAwgYEAAaDDYzNzQyMzE4MzgwNSIMYhP5DwB10bX46MeFKtwDZ7yzU03ATo747fx9Jmby0zfzflfJ48Fu84So7Qj1bxg1L09WX9kJiM048%2BvdBu83KNiRwNqEMAcqqs9UcbRt%2FM8k%2BtFJpBs6v6viF7sVip4wjrg6a255ukCCV20NPe76y0QnGZ3Qt7jm6r3g3kQvfFy3ad5PeNd1UxtiyjZ0lbFBE65tU0V1H2nn8mUISMylSnAtlH6rQ8JApOhLtvwd36LOULnz%2Bgq5p4PmlL4PvasmaN2GOFURfzKmD5UGUss8rfWGLPYUVbOlQF95ZJcHK2DV2SBSHdxZRMYRDmfHFnJOdf85zuByhaAaRzCzbjRQvdpm1C6mhp7mpnjJ4oSqk1%2FL2HzBxtqdlsOMTHVtq9QQB6rIhsBumRiI2uUm3XGhdEgOL%2Bh1QTTEhnfetGJueE7DMRXGfVjIGTYNT2%2F4UIrjkrEcuz44wuMNxIbxwEKU9zpuVSmeP4PI5Soigkmpt6a%2BZbp1XD81eT1%2BmglfVM9GBbSyOkFb3ocZU0kVeETc0jhBMCf51HMEVs6kuuJverRZVdF5nP8%2BWPa11PGlB8jCMTF6yeJVsniR%2F0Sx62QQWg50ZPDT3PSRKRX2eeZDJ0vTq3l5fPAMTDFJwICcAWVOq%2FludvaWSEKFnhowmcSR0wY6pgHhrT%2Bb3CnjFnB%2BFFmjkRRMl6HlTh4Oken0qakkf1fsuHOnMIr1ty6Ro1ekmxATso908dIc7VxAS10PJZ%2BThRebOzJPlbaYLcU00zxk77MR9mzGBragYLRpwVxy4BCco3AnG%2BgE0vEtMIIahuBicYth7OTh9z5gCrTh4VqgTOIuHMH6F%2FlMNdrk1hEO1w3Fp2o3%2Bfr1TWDDVlPSNgCvz24xnk8rpHSz&X-Amz-Signature=efb4c19b2a20d794d116575e8ef0260dc78d6fcebf9bbbb5aa253a3e7e9891f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







