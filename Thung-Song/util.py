import pandas as pd
import numpy as np
import os
import math
import requests

def NEW_getMaxTandMinT(df):
    
    """
    Function to calculate the maximum and minimum temperatures for each date
    and aggregate other variables for the same date.
    """
    
    date = []
    ndate = 'date'

    v1 = []
    nv1 = "u10"
    v2 = []
    nv2 = "v10"
    v3 = []
    nv3 = "d2m"
    v4 = []
    nv4 = "meanTemp"
    v5 = []
    nv5 = "uvb"
    v6 = []
    nv6 = "e"
    v7 = []
    nv7 = "stl1"
    v8 = []
    nv8 = "sp"
    v9 = []
    nv9 = "tp"
    
    v10 = []
    nv10 = "maxTemp"
    v11 = []
    nv11 = "minTemp"
    
    
    nlat = "lat"
    lat = []
    nlng= 'lng'
    lng = []
        
        
    saveTmp = []
    collect = [0,0,0,0,0,0,0,0,0]
    collectNum = 0
    i=-1
    while( i < len(df)-1 )  :
        i=i+1
        if( (i>=len(df)-1) ):
            saveTmp.append(df.loc[i, "t2m"])
            for k in range(len(collect)):
                if(k==0):
                    col = "u10"
                elif(k==1):
                    col = "v10"
                elif(k==2):
                    col = "d2m"
                elif(k==3):
                    col = "t2m"
                elif(k==4):
                    col = "uvb"
                elif(k==5):
                    col = "e"
                elif(k==6):
                    col = "stl1"
                elif(k==7):
                    col = "sp"
                elif(k==8):
                    col = "tp"
                collect[k] = collect[k] + df.loc[i, col]
            collectNum=collectNum+1
            
            
            date.append( df.loc[i-1, "time"].split("T")[0] )
            v11.append( min(saveTmp) )
            v10.append( max(saveTmp) )
            
            for k in range(len(collect)):
                if(k==0):
                    v1.append(collect[k]/collectNum)
                elif(k==1):
                    v2.append(collect[k]/collectNum)
                elif(k==2):
                    v3.append(collect[k]/collectNum)
                elif(k==3):
                    v4.append(collect[k]/collectNum)
                elif(k==4):
                    v5.append(collect[k]/collectNum)
                elif(k==5):
                    v6.append(collect[k]/collectNum)
                elif(k==6):
                    v7.append(collect[k]/collectNum)
                elif(k==7):
                    v8.append(collect[k]/collectNum)
                elif(k==8):
                    v9.append(collect[k]/collectNum)
            collectNum=0
            saveTmp=[]
            collect = [0,0,0,0,0,0,0,0,0]
            
            lng.append(df.loc[i-1, "longitude"])
            lat.append(df.loc[i-1, "latitude"])

            
            
        elif( (i>=1 and df.loc[i, "time"].split("T")[0] == df.loc[i-1, "time"].split("T")[0] ) or i==0 ):
            saveTmp.append(df.loc[i, "t2m"])
            for k in range(len(collect)):
                if(k==0):
                    col = "u10"
                elif(k==1):
                    col = "v10"
                elif(k==2):
                    col = "d2m"
                elif(k==3):
                    col = "t2m"
                elif(k==4):
                    col = "uvb"
                elif(k==5):
                    col = "e"
                elif(k==6):
                    col = "stl1"
                elif(k==7):
                    col = "sp"
                elif(k==8):
                    col = "tp"
                collect[k] = collect[k] + df.loc[i, col]
            collectNum=collectNum+1
            
        elif( (i>=1 and df.loc[i, "time"].split("T")[0] != df.loc[i-1, "time"].split("T")[0]) ):
            date.append( df.loc[i-1, "time"].split("T")[0] )
            v11.append( min(saveTmp) )
            v10.append( max(saveTmp) )
            
            for k in range(len(collect)):
                if(k==0):
                    v1.append(collect[k]/collectNum)
                elif(k==1):
                    v2.append(collect[k]/collectNum)
                elif(k==2):
                    v3.append(collect[k]/collectNum)
                elif(k==3):
                    v4.append(collect[k]/collectNum)
                elif(k==4):
                    v5.append(collect[k]/collectNum)
                elif(k==5):
                    v6.append(collect[k]/collectNum)
                elif(k==6):
                    v7.append(collect[k]/collectNum)
                elif(k==7):
                    v8.append(collect[k]/collectNum)
                elif(k==8):
                    v9.append(collect[k]/collectNum)
            collectNum=0
            saveTmp=[]
            lng.append(df.loc[i-1, "longitude"])
            lat.append(df.loc[i-1, "latitude"])
            collect = [0,0,0,0,0,0,0,0,0]
            
            
            saveTmp.append(df.loc[i, "t2m"])
            for k in range(len(collect)):
                if(k==0):
                    col = "u10"
                elif(k==1):
                    col = "v10"
                elif(k==2):
                    col = "d2m"
                elif(k==3):
                    col = "t2m"
                elif(k==4):
                    col = "uvb"
                elif(k==5):
                    col = "e"
                elif(k==6):
                    col = "stl1"
                elif(k==7):
                    col = "sp"
                elif(k==8):
                    col = "tp"
                collect[k] = collect[k] + df.loc[i, col]
            collectNum=collectNum+1
            
            
    df2 = pd.DataFrame({ndate:date,
                        nlat:lat,
                        nlng:lng,
                        nv1:v1,
                        nv2:v2,
                        nv3:v3,
                        nv11:v11,
                        nv4:v4,
                        nv10:v10,
                        nv5:v5,
                        nv6:v6,
                        nv7:v7,
                        nv8:v8,
                        nv9:v9

                       })

    
    return df2
        
    

def NEW_dateD(df):
    """
    Function to format the 'date' column in a DataFrame to the 'dd/mm/YYYY' format.
    """
    
    i=-1
    while( i < len(df)-1 )  :
        i=i+1
#         print(df.loc[i, "date"]+"changed to ")
        date = df.loc[i, "date"];
        x = date.split("-")
        x[0] = f"{int(x[0]):02}"
        x[1] = f"{int(x[1]):02}"
        
        date = str(x[0])+"/"+str(x[1])+"/"+str(x[2])
        df.at[i, 'date'] = str(date)
#         print(date)
        df.style.format({"date": lambda t: t.strftime("%dd/%mm/%YYYY")})
        df["date"] = df["date"].astype(str)
    return df


def NEW_RHnWS(df):
    
    """
    Function to calculate Relative Humidity (RH) and Wind Speed (WS) from existing columns
    in the DataFrame and add them as new columns.
    """
    
    v1 = []
    nv1 = "RH"
    v2 = []
    nv2 = "WS"
    v3 = []
    nv3 = "d2m"
    v4 = []
    nv4 = "meanTemp"
    v5 = []
    nv5 = "minTemp"
    v6 = []
    nv6 = "maxTemp"
    
    i=-1
    while( i < len(df)-1 )  :
        i=i+1
        
        
        eT = 6.112*np.exp( (17.62*(float(df.loc[i, "meanTemp"])-272.15) / (243.12+ (float(df.loc[i, "meanTemp"])-272.15) ) )  )
        fp = 1.0016 + (3.15*float(df.loc[i, "sp"])*0.01)*pow(10,-6) - 0.074/(float(df.loc[i, "sp"])*0.01)
        eTd = 6.112*np.exp( (17.62*(float(df.loc[i, "d2m"])-272.15) / (243.12+ (float(df.loc[i, "d2m"])-272.15) ) )  )
        
        epTd = fp*eTd
        epT = fp*eT
        RH = epTd/epT
        
        v1.append(RH)
        
        
        s = np.sqrt(pow(float(df.loc[i, "u10"]),2) + pow(float(df.loc[i, "v10"]),2))
        v2.append(s)
        
        v3.append( float(df.loc[i, "d2m"])-272.15 )
        v4.append( float(df.loc[i, "meanTemp"])-272.15 )
        v5.append( float(df.loc[i, "minTemp"])-272.15 )
        v6.append( float(df.loc[i, "maxTemp"])-272.15 )
        
    
    df = df.drop(columns=["u10","v10","minTemp","maxTemp","meanTemp","d2m"])
      
        
    df[nv3]=v3
    df[nv5]=v5
    df[nv4]=v4
    df[nv6]=v6
    df[nv1]=v1
    df[nv2]=v2
    

    return df