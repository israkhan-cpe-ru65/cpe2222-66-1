def main():
    dataOfPeter = dict({
        "name": "Peter",
        "age": 40,
        "gender": "Male",  
        "test": {
            "first": 20,
            "second": 18,
            "third": 19
        }
    })
    
    dataOfPaul = dict({
        "name": "Paul",
        "age": 25,
        "gender": "Male",  
        "test": {
            "first": 19,
            "second": 20,
            "third": 19
        }
    })
    
    dataOfMary = dict({
        "name": "Mary",
        "age": 18,
        "gender": "Female",  
        "test": {
            "first": 10,
            "second": 5,
            "third": 4
        }
    })
    
    dataOfJenny = dict({
        "name": "Jenny",
        "age": 60,
        "gender": "Female",  
        "test": {
            "first": 5,
            "second": 3,
            "third": 1
        }
    })
    
    data = dict(
        peter = dataOfPeter,
        paul = dataOfPaul,
        mary = dataOfMary,
        jenny = dataOfJenny)

    dataOfRobert = {
        "name": "Robert",
        "age": 35,
        "gender": "Male",  
        "test": {
            "first": 10,
            "second": 18,
            "third":5
        }
    }
    
    data.update(robert = dataOfRobert)
    
    print("\"Peter\" is", data["peter"]["gender"])
    print("The 1st test score of \"Mary\" is", data["mary"]["test"]["first"])
    print("The 2nd test score of \"Jenny\" is", data["jenny"]["test"]["second"])
    print("The 3rd test score of \"Paul\" is", data["paul"]["test"]["third"])
    print("\"Robert\" is", data["robert"]["age"], "years old")
    print("The dictionary to solve this problem was designed as:\n", data)
    
    return


if __name__ == '__main__':
    main()    
    
