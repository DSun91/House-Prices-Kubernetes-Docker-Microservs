import pandas as pd
import sqlite3
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

class CreateDB:
    def CreateDb(self,df, DbName, table_name):
        # Step 2: Create a connection to the SQLite database
        conn = sqlite3.connect(DbName)  # This will create the database if it doesn't exist
        cursor = conn.cursor()

        # Step 3: Create a table and insert the data
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Step 4: Commit the transaction and close the connection
        conn.commit()
        conn.close()

    def ReadDb(self,query, DbName):
        # Step 1: Connect to the SQLite database
        conn = sqlite3.connect(DbName)  # Replace with your database name
        cursor = conn.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        # Step 4: Get column names
        column_names = [description[0] for description in cursor.description]

        # Step 5: Convert the results into a pandas DataFrame (optional)
        df = pd.DataFrame(rows, columns=column_names)

        df=df.reset_index(drop=True)
        # Step 6: Close the connection
        conn.close()

        # Print the DataFrame to see the data
        return df

    def CreateAllDBs(self):


        dfComplete = pd.read_csv("House Price India.csv")

        dfGeoLoc = dfComplete[['id', 'Postal Code', 'Lattitude', 'Longitude']]

        dfNeighbor = dfComplete[['id', 'No of schools nearby', 'Distance from the airport']]

        dfBusinessInsight = dfComplete[['id', 'No of views']]

        dfPrice = dfComplete[['id', 'Price']]

        dfComplete.drop(['Postal Code', 'Lattitude', 'Longitude', 'No of schools nearby', 'Distance from the airport',
                         'No of views', 'Price'], axis=1, inplace=True)

        self.CreateDb(dfComplete, "MicroSpecs/HousesSpecsDb.db", "ATable")

        self.CreateDb(dfGeoLoc, "MicroGeoLoc/HousesDbGeoLoc.db", "ATable")

        self.CreateDb(dfNeighbor, "MicroNeighbor/HousesDbNeighbor.db", "ATable")

        self.CreateDb(dfBusinessInsight, "MicroBusinessInsight/HousesDbBusinessInsight.db", "ATable")

        self.CreateDb(dfPrice, "MicroPrices/HousesDbPrice.db", "ATable")

        #print(dfComplete)






#dbCreator=CreateDB()
#dbCreator.CreateAllDBs()

