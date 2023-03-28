#include "thread.h"
#include "socket.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace Sync;

// class ClientThread : public Thread {
// 	private:
// 		Socket& socket;
// 		bool& active;
// 		std:String str;
	
// 	public:


// }


int main(void)
{
	std::cout << "I am a client" << std::endl;
	// bool active = true;

	// Create Socket
	Socket socket("10.0.2.15", 2000);
	socket.Open();

	std::string str;

	while(true)
	{
		try
		{
			bool validInput = false;
			while(!validInput)
			{
				std::cout << "Input a string (or type 'done' to exit): ";
				std::cout.flush();
				std::getline(std::cin, str);
				if(str != "")
				{
					validInput = true;
				}
			}
			

			ByteArray data = ByteArray(str);

			socket.Write(data);


			if(str == "done")
			{
				std::cout << "Closing socket as directed" << std::endl;
				break;
			}

			int res = socket.Read(data);

			if(res == 0)
			{
				std::cout << "Server has been terminated, closing socket" << std::endl;
				break;
			}

			std::cout << "Server Response: " << data.ToString() << std::endl;
		}
		catch(std::string err)
		{
			std::cout << err << std::endl;
		}
		catch(TerminationException terminationException)
		{
			std::cout << "termination" << std::endl;
			return terminationException;
		}
	}

	std::cout << "Socket closed" << std::endl;

	socket.Close();

	return 0;
}
