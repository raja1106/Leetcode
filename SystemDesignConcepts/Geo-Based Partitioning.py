# Define partitions for different geographic regions
class GeoPartition:
    def __init__(self, region_name):
        self.region_name = region_name
        self.data = []

    def insert(self, row):
        self.data.append(row)
        print(f"Inserted data for user {row['user_id']} into {self.region_name} partition.")

    def query(self, user_id):
        for row in self.data:
            if row['user_id'] == user_id:
                return row
        return None

class GeoPartitionedTable:
    def __init__(self):
        # Set up regional partitions
        self.partitions = {
            "North America": GeoPartition("North America"),
            "Europe": GeoPartition("Europe"),
            "Asia": GeoPartition("Asia")
        }

    def get_region(self, location):
        # Example mapping function to assign region based on location
        if location in ["USA", "Canada", "Mexico"]:
            return "North America"
        elif location in ["UK", "Germany", "France"]:
            return "Europe"
        elif location in ["India", "China", "Japan"]:
            return "Asia"
        else:
            return None

    def insert(self, row):
        # Determine region based on user location and insert into the appropriate partition
        region = self.get_region(row['location'])
        if region:
            self.partitions[region].insert(row)
        else:
            print(f"No partition found for location: {row['location']}")

    def query(self, user_id, location):
        # Determine region based on location and query the appropriate partition
        region = self.get_region(location)
        if region:
            result = self.partitions[region].query(user_id)
            if result:
                print(f"Data found in {region} partition.")
            else:
                print(f"No data found for user {user_id} in {region} partition.")
            return result
        else:
            print(f"No partition found for location: {location}")
            return None

# Example usage
table = GeoPartitionedTable()

# Insert data with location-based routing
table.insert({"user_id": 101, "name": "Alice", "location": "USA"})
table.insert({"user_id": 102, "name": "Bob", "location": "Germany"})
table.insert({"user_id": 103, "name": "Charlie", "location": "India"})

# Query data based on user location
result = table.query(102, "Germany")  # Query from Europe partition
print("Query result:", result)

# Check the data distribution across partitions
for region, partition in table.partitions.items():
    print(f"{region} Partition:", partition.data)
