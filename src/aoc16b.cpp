#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_set>
#include <chrono>

#include <boost/container_hash/hash.hpp>

using namespace std;
using namespace boost;

class turn_data
{
public:
	int remaining_turns = 26;
	int pressure = 0;
	int curr_rate = 0;
	vector<string> pos{ "AA", "AA"};
	set<string> done;
	vector<string> came_from{"", ""};
};
bool operator<(const turn_data& s1, const turn_data& s2)
{
	if (s1.remaining_turns == s2.remaining_turns)
	{
		if (s1.pressure == s2.pressure)
		{
			return s1.curr_rate < s2.curr_rate;
		}
		else
		{
			return s1.pressure < s2.pressure;
		}
	}
	else
	{
		return s1.remaining_turns < s2.remaining_turns;
	}
}



class key
{
public:
	bool operator==(const key& t) const
	{
		return this->pos[0] == t.pos[0] && this->pos[1] == t.pos[1] && this->curr_rate == t.curr_rate;
	}

	vector<string> pos;
	int curr_rate = 0;

};

class KeyHasher {
public:
	// id is returned as hash function
	size_t operator()(const key& k) const
	{
		size_t result = 0;
		hash_combine(result, k.pos[0]);
		hash_combine(result, k.pos[1]);
		hash_combine(result, k.curr_rate);
		return result;
	}
};


int main()
{
	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
	fstream inputfile;
	inputfile.open("ex16.txt", ios::in);
	string line;
	vector<string> names;
	map<string, int> rates;
	map<string, vector<string>> neighbors;

	while (getline(inputfile, line))
	{
		string delimiter = " ";
		size_t pos = 0;
		string token, name;
		int i = 0;
//		while ((pos = line.find(delimiter)) != std::string::npos) {
		while (line.size() > 0) {
			pos = line.find(delimiter);
			token = line.substr(0, pos);
			if (i == 1)
			{
				name = token;
				names.push_back(token);
			}
			else if(i == 4) 
			{
				size_t end = token.find(';');
				rates[name] = stoi(token.substr(5, end));
			}
			else if(i > 8)
			{
				token.erase(std::remove(token.begin(), token.end(), ','), token.end());
				neighbors[name].push_back(token);
			}
			if (pos == string::npos)
			{
				line = "";
			}
			else
			{
				line.erase(0, pos + delimiter.length());

			}
			i++;
		}

	}
	turn_data initial_data = turn_data();
	priority_queue<turn_data> q;
	q.push(initial_data);

	unordered_set<key, KeyHasher> memory;
	int rem_last_step = 26;
	int n_skipped = 0;

	while (!q.empty()) {
		turn_data td = q.top();
		q.pop();
		if (td.remaining_turns < rem_last_step)
		{
			//memory.erase(memory.begin(), memory.end());
			rem_last_step = td.remaining_turns;
			memory.clear();
			cout << "remaining steps: " << rem_last_step << ", current pressure: " << td.pressure 
				 << ", current remaining iterations: " << q.size() << " n_skipped: " << n_skipped << endl;
			if (rem_last_step == 0)
			{
				cout << "final pressure: " << td.pressure << endl;
				std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
				std::cout << "Time difference = " << std::chrono::duration_cast<std::chrono::seconds>(end - begin).count() << "[s]" << std::endl;
				break;
			}
		}
		key k;
		if (td.pos[0] > td.pos[1])
		{
			k.pos = td.pos;
		}
		else
		{
			k.pos.push_back(td.pos[1]);
			k.pos.push_back(td.pos[0]);
		}
		k.curr_rate = td.curr_rate;
		if (memory.find(k) != memory.end())
		{
			n_skipped++;
			continue;
		}
		memory.insert(k);
		td.pressure += td.curr_rate;
		pair<vector<pair<int, string> >, vector<pair<int, string> > > changes;
		for (int i = 0; i < 2; ++i)
		{
			if (rates[td.pos[i]] > 0 and td.done.find(td.pos[i]) == td.done.end() and (i == 0 or td.pos[0] != td.pos[1]))
			{
				if (i == 0)
				{
					changes.first.push_back(make_pair(0, ""));
				}
				else
				{
					changes.second.push_back(make_pair(0, ""));
				}
			}

			for (auto& n : neighbors[td.pos[i]])
			{
				if (td.came_from[i] != n or (neighbors[td.pos[i]].size() == 1))
				{
					if (i == 0)
					{
						changes.first.push_back(make_pair(1, n));
					}
					else
					{
						changes.second.push_back(make_pair(1, n));
					}
				}
			}
		}
		for (auto& c1 : changes.first)
		{
			for (auto& c2 : changes.second)
			{
				turn_data new_td = td;
				new_td.remaining_turns--;
				new_td.came_from = td.pos;
				if (c1.first == 0)
				{
					new_td.curr_rate += rates[td.pos[0]];
					new_td.done.insert(td.pos[0]);
				}
				else
				{
					new_td.pos[0] = c1.second;
					new_td.came_from[0] = td.pos[0];
				}
				if (c2.first == 0)
				{
					new_td.curr_rate += rates[td.pos[1]];
					new_td.done.insert(td.pos[1]);
				}
				else
				{
					new_td.pos[1] = c2.second;
					new_td.came_from[1] = td.pos[1];
				}
				q.push(new_td);
			}
		}
	}
}




