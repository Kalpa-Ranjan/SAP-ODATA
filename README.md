



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RRJZXIR%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T051646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDuSQA3ckol%2FOk%2BResusV09knDGDTjVAGE%2B%2FyjtOn%2BDXAiBL0wG62%2F4x6dGbsy%2BPXwMnszrlEmG7icgWfXpfuopuhSr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMcadryFBsnU4sLWzOKtwD7im5PqApAvhNX%2F5N3n45DrBlUVFMUN1IWXVOAyJejwLvMnsL6KfEn9Lq5doALZRNto5q%2BQhFhrgqtzWS60cWKsEODnHIYOioUQR9C%2BGKTzZXUO2za0mzYgG%2BPwU06iTLuO%2F%2FfOIKXwE0v2CxfVZPWW8twP7oC22F7dQWipLeMAg8aKZ3vmDl2DRLmgSlUJBLHN3t5qaxGVwsUMDpquR%2BcZCapDVWQTe4C%2F%2B3%2FG2pTX2wlC%2BZZkZbcfKrUCKJRVv%2Bn6SKXVJBmYLM9pA4go7krwYaYF3nvHvWnbPGta0gfNnM42hFFgucH3SsogBfLPp8%2FiF0sOJ2ZzrslttsSAKvy24cv7OpWZsbi7145obdvp5LGVJR1fZOfLokHC5waOXc2F2GV2ftBgF7BQwOJFaerTAIaLbDznafXB75fmc2oVOO0pMn2nR3sU5s4Ts2aLPlleCECl632K0%2B0Y0P7jXbZpOeyKmm5%2FSjWaRAbi7RG%2F804kfTij%2FrRbrHZ18lkn9CQcY3w4Dh4EdAKli9bFPJ7fT0ogpMl5LDA0kpufAC5fy3M%2FLhTRD0xTRrfTjEqKTB8C1ujsRbX%2BUqhVFHfnbzzW17ZnCEqXyooukxUjnV43YCJcjh%2FrvNTk0Cg%2Fww0tHJ1AY6pgEOCOotHj0TlX0jcVwzQzmEx9kz6DwQ5wDfbWh1dMAr1gTdYgap7lch199bMIImHHFwzOEHJYuJr9%2FeFfrouocN%2B76Ug5gTszUBH%2FdTgXjJARX8kwZaCHwmfbXh7ARL2MISIDLmdOKhdag9WAsdKVCU9%2BaEeYxl%2FhUrEaz8oF%2BZBrCpRHWW4Z%2Fam0Lkss2iEHnPqfp0PgtrxTCPLKMGAe4uAfNCXpEI&X-Amz-Signature=b914d0ed438414face60eed6c5595e36e8d5e6eeb92b253145d419a08f4a13cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RRJZXIR%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T051646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDuSQA3ckol%2FOk%2BResusV09knDGDTjVAGE%2B%2FyjtOn%2BDXAiBL0wG62%2F4x6dGbsy%2BPXwMnszrlEmG7icgWfXpfuopuhSr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMcadryFBsnU4sLWzOKtwD7im5PqApAvhNX%2F5N3n45DrBlUVFMUN1IWXVOAyJejwLvMnsL6KfEn9Lq5doALZRNto5q%2BQhFhrgqtzWS60cWKsEODnHIYOioUQR9C%2BGKTzZXUO2za0mzYgG%2BPwU06iTLuO%2F%2FfOIKXwE0v2CxfVZPWW8twP7oC22F7dQWipLeMAg8aKZ3vmDl2DRLmgSlUJBLHN3t5qaxGVwsUMDpquR%2BcZCapDVWQTe4C%2F%2B3%2FG2pTX2wlC%2BZZkZbcfKrUCKJRVv%2Bn6SKXVJBmYLM9pA4go7krwYaYF3nvHvWnbPGta0gfNnM42hFFgucH3SsogBfLPp8%2FiF0sOJ2ZzrslttsSAKvy24cv7OpWZsbi7145obdvp5LGVJR1fZOfLokHC5waOXc2F2GV2ftBgF7BQwOJFaerTAIaLbDznafXB75fmc2oVOO0pMn2nR3sU5s4Ts2aLPlleCECl632K0%2B0Y0P7jXbZpOeyKmm5%2FSjWaRAbi7RG%2F804kfTij%2FrRbrHZ18lkn9CQcY3w4Dh4EdAKli9bFPJ7fT0ogpMl5LDA0kpufAC5fy3M%2FLhTRD0xTRrfTjEqKTB8C1ujsRbX%2BUqhVFHfnbzzW17ZnCEqXyooukxUjnV43YCJcjh%2FrvNTk0Cg%2Fww0tHJ1AY6pgEOCOotHj0TlX0jcVwzQzmEx9kz6DwQ5wDfbWh1dMAr1gTdYgap7lch199bMIImHHFwzOEHJYuJr9%2FeFfrouocN%2B76Ug5gTszUBH%2FdTgXjJARX8kwZaCHwmfbXh7ARL2MISIDLmdOKhdag9WAsdKVCU9%2BaEeYxl%2FhUrEaz8oF%2BZBrCpRHWW4Z%2Fam0Lkss2iEHnPqfp0PgtrxTCPLKMGAe4uAfNCXpEI&X-Amz-Signature=6043b112c502c991994aeafd689e812b1d51f83c15b0c15b6c4c97dab44c380f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







